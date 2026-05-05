# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T03:45:18.539374+00:00`
- Correlation status: `ready`
- Asset price records: `325`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `7`; crypto_alt avg `-0.0704` n `223`; crypto_major avg `0.2575` n `7`; equity avg `0.107` n `47`; fx avg `0.0005` n `4`; index avg `0.0155` n `6`; metal avg `-0.0321` n `7`; unknown avg `-0.1046` n `312`
- 1h: commodity avg `0.1402` n `7`; crypto_alt avg `-0.0472` n `223`; crypto_major avg `0.1893` n `7`; equity avg `0.0187` n `47`; fx avg `-0.0067` n `4`; index avg `0.0546` n `6`; metal avg `-0.2425` n `7`; unknown avg `-0.1214` n `312`
- 4h: commodity avg `-0.2232` n `7`; crypto_alt avg `1.0582` n `223`; crypto_major avg `1.278` n `7`; equity avg `0.6054` n `47`; fx avg `-0.011` n `4`; index avg `0.1706` n `6`; metal avg `0.4804` n `7`; unknown avg `0.2854` n `312`
- 24h: commodity avg `0.9997` n `7`; crypto_alt avg `0.9613` n `223`; crypto_major avg `0.2385` n `7`; equity avg `-0.8884` n `47`; fx avg `0.0009` n `4`; index avg `-0.2082` n `6`; metal avg `-1.9082` n `7`; unknown avg `-1.3399` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2268`, n `321`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2203`, n `321`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1516`, n `321`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1416`, n `321`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1406`, n `317`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.138`, n `317`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `321`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `321`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1246`, n `321`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `317`, weak_sample_signal
