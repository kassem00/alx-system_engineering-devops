// Load this script as sslshoppercom-bsa.js
(() => {
	var script = document.createElement('script');
	script.id = '_monetization_js';
	script.type = 'text/javascript';
	script.src =
		'//m.servedby-buysellads.com/monetization.js';
	script.async = true;
	document.head.appendChild(script);

	script.onload = function () {
		_bsa.init(
			'custom',
			'CWYIV2QE',
			'placement:sslshoppercom-sticky',
			{
				target: '#bsa-zone_1702413719716-6_123456',
				id: 'standard',
				template: `
<div class="bsaNativeResponsive">
	<a href="##statlink##" class="bsaNativeResponsiveChild" style="background: ##backgroundColor##" rel="sponsored noopener" target="_blank" title="##company## — ##tagline##">
		<img class="bsaNativeResponsiveLogo" width="125" src="##logo##" alt="##company## logo" loading="lazy"/>
		<div class="bsaNativeResponsiveText">
			<div class="bsaNativeResponsiveDetails" style="color: ##textColor##;border-left: solid 1px ##textColor##;">
				<span class="bsaNativeResponsiveCompany">
					Sponsored by ##company##
				</span>
				<span class="bsaNativeResponsiveDescription">
					##description##
				</span>
			</div>
			<span class="bsaNativeResponsiveButton" style="color: ##ctaTextColor##;background-color: ##ctaBackgroundColor##;">
				##callToAction##
			</span>
		</div>
	</a>
</div>
`,
			}
		);
	};
})();

const BSANativeCallback = (req) => {
	if (req.ads.length === 0) {
		window.isOptimizeLoaded =
			window.isOptimizeLoaded || false;
		window.optimizeTargetIds =
			window.optimizeTargetIds || [];
		window.optimizeTargetIds.push(
			req.options.target.replace('#', '')
		);
		if (!window.isOptimizeLoaded) {
			const bsa_optimize = document.createElement('script');
			bsa_optimize.type = 'text/javascript';
			bsa_optimize.async = true;
			bsa_optimize.src =
				'https://cdn4.buysellads.net/pub/sslshopper.js?' +
				(new Date() - (new Date() % 600000));
			(
				document.getElementsByTagName('head')[0] ||
				document.getElementsByTagName('body')[0]
			).appendChild(bsa_optimize);
			window.isOptimizeLoaded = true;
			async function isOptimizeInitialized() {
				while (
					window.optimize.isInitialized === undefined
				) {
					await new Promise((resolve) =>
						setTimeout(resolve, 100)
					);
				}
			}
			bsa_optimize.addEventListener('load', () => {
				window.optimize = window.optimize || {
					queue: [],
				};
				window.optimize.queue.push(() => {
					(async () => {
						await isOptimizeInitialized();
						window.optimize.push(window.optimizeTargetIds);
					})();
				});
			});
		}
	}
};