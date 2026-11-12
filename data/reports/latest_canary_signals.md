# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T16:07:28.796599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.709` n `239`; crypto_major avg `0.6455` n `8`; equity avg `0.9826` n `162`; fx avg `0.0072` n `6`; index avg `0.0928` n `27`; metal avg `0.1027` n `20`; unknown avg `1.0005` n `1247`
- 1h: commodity avg `-0.1238` n `13`; crypto_alt avg `1.0759` n `239`; crypto_major avg `1.0332` n `8`; equity avg `2.0357` n `162`; fx avg `-0.0209` n `6`; index avg `0.1885` n `27`; metal avg `0.1359` n `20`; unknown avg `6.1472` n `1243`
- 4h: commodity avg `0.2071` n `13`; crypto_alt avg `-0.0654` n `239`; crypto_major avg `-0.2231` n `8`; equity avg `0.7801` n `162`; fx avg `-0.0286` n `6`; index avg `0.1652` n `27`; metal avg `-0.3578` n `20`; unknown avg `1.1958` n `1239`
- 24h: commodity avg `-0.2372` n `13`; crypto_alt avg `-3.2118` n `239`; crypto_major avg `-2.7924` n `8`; equity avg `-2.001` n `162`; fx avg `-0.1333` n `6`; index avg `-0.0343` n `27`; metal avg `-0.9809` n `20`; unknown avg `2.544` n `1148`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
