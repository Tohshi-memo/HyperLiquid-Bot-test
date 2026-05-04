# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T20:15:25.787567+00:00`
- Correlation status: `ready`
- Asset price records: `295`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0783` n `7`; crypto_alt avg `0.0985` n `223`; crypto_major avg `0.1007` n `7`; equity avg `-0.0061` n `47`; fx avg `0.0122` n `4`; index avg `-0.0624` n `6`; metal avg `-0.0705` n `7`; unknown avg `-0.0142` n `312`
- 1h: commodity avg `-0.0799` n `7`; crypto_alt avg `-0.1369` n `223`; crypto_major avg `-0.1156` n `7`; equity avg `-0.3305` n `47`; fx avg `0.0132` n `4`; index avg `0.0715` n `6`; metal avg `-0.1358` n `7`; unknown avg `0.0277` n `312`
- 4h: commodity avg `-0.0975` n `7`; crypto_alt avg `0.1582` n `223`; crypto_major avg `-0.1554` n `7`; equity avg `-0.4548` n `47`; fx avg `-0.0008` n `4`; index avg `-0.1059` n `6`; metal avg `-0.0948` n `7`; unknown avg `-0.2892` n `312`
- 24h: commodity avg `1.4858` n `7`; crypto_alt avg `1.4836` n `223`; crypto_major avg `0.8204` n `7`; equity avg `-0.3876` n `47`; fx avg `-0.0923` n `4`; index avg `-0.0708` n `6`; metal avg `-2.4199` n `7`; unknown avg `-1.0679` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2365`, n `291`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2307`, n `291`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.177`, n `287`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1757`, n `287`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1503`, n `291`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `291`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1437`, n `291`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `291`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `287`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1206`, n `291`, weak_sample_signal
