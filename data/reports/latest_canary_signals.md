# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T21:45:26.542434+00:00`
- Correlation status: `ready`
- Asset price records: `301`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0373` n `7`; crypto_alt avg `0.0491` n `223`; crypto_major avg `0.0656` n `7`; equity avg `0.0036` n `47`; fx avg `-0.0037` n `4`; index avg `-0.1186` n `6`; metal avg `0.0144` n `7`; unknown avg `-0.0867` n `312`
- 1h: commodity avg `0.0567` n `7`; crypto_alt avg `0.6274` n `223`; crypto_major avg `0.4566` n `7`; equity avg `0.1051` n `47`; fx avg `-0.009` n `4`; index avg `-0.1595` n `6`; metal avg `0.088` n `7`; unknown avg `-0.1643` n `312`
- 4h: commodity avg `-0.0954` n `7`; crypto_alt avg `-0.1056` n `223`; crypto_major avg `-0.3572` n `7`; equity avg `-0.3833` n `47`; fx avg `-0.0053` n `4`; index avg `-0.0894` n `6`; metal avg `-0.0584` n `7`; unknown avg `-0.412` n `312`
- 24h: commodity avg `2.1151` n `7`; crypto_alt avg `2.4502` n `223`; crypto_major avg `1.5656` n `7`; equity avg `-0.3854` n `47`; fx avg `-0.0356` n `4`; index avg `-0.2894` n `6`; metal avg `-2.4413` n `7`; unknown avg `-1.0921` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2357`, n `297`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2298`, n `297`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1785`, n `293`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1772`, n `293`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `297`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.148`, n `297`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `297`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1306`, n `297`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.121`, n `293`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1198`, n `297`, weak_sample_signal
