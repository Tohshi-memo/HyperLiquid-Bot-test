# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T23:15:24.299035+00:00`
- Correlation status: `ready`
- Asset price records: `307`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `7`; crypto_alt avg `-0.1574` n `223`; crypto_major avg `-0.1168` n `7`; equity avg `-0.0338` n `47`; fx avg `-0.0005` n `4`; index avg `0.0167` n `6`; metal avg `0.0732` n `7`; unknown avg `0.0435` n `312`
- 1h: commodity avg `0.0223` n `7`; crypto_alt avg `-0.4715` n `223`; crypto_major avg `-0.3352` n `7`; equity avg `-0.399` n `47`; fx avg `0.0027` n `4`; index avg `-0.022` n `6`; metal avg `-0.0548` n `7`; unknown avg `-0.0274` n `312`
- 4h: commodity avg `-0.0571` n `7`; crypto_alt avg `-0.319` n `223`; crypto_major avg `-0.2074` n `7`; equity avg `-0.5085` n `47`; fx avg `0.0155` n `4`; index avg `-0.0997` n `6`; metal avg `-0.1018` n `7`; unknown avg `-0.0532` n `312`
- 24h: commodity avg `1.527` n `7`; crypto_alt avg `1.4954` n `223`; crypto_major avg `0.4318` n `7`; equity avg `-0.4591` n `47`; fx avg `-0.0172` n `4`; index avg `-0.1692` n `6`; metal avg `-2.3603` n `7`; unknown avg `-1.2076` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2359`, n `303`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2301`, n `303`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1796`, n `299`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1779`, n `299`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `303`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `303`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1414`, n `303`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `303`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1206`, n `303`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `299`, weak_sample_signal
