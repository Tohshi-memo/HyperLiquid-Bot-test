# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T04:15:24.606343+00:00`
- Correlation status: `ready`
- Asset price records: `327`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `7`; crypto_alt avg `-0.0905` n `223`; crypto_major avg `-0.0909` n `7`; equity avg `-0.0082` n `47`; fx avg `0.0008` n `4`; index avg `0.0207` n `6`; metal avg `0.0293` n `7`; unknown avg `0.0643` n `312`
- 1h: commodity avg `0.06` n `7`; crypto_alt avg `0.0024` n `223`; crypto_major avg `0.1735` n `7`; equity avg `-0.1316` n `47`; fx avg `0.0024` n `4`; index avg `0.0522` n `6`; metal avg `-0.204` n `7`; unknown avg `-0.1053` n `312`
- 4h: commodity avg `-0.1407` n `7`; crypto_alt avg `0.6976` n `223`; crypto_major avg `0.951` n `7`; equity avg `0.4236` n `47`; fx avg `-0.0073` n `4`; index avg `0.1856` n `6`; metal avg `0.3116` n `7`; unknown avg `0.2152` n `312`
- 24h: commodity avg `1.1183` n `7`; crypto_alt avg `0.2883` n `223`; crypto_major avg `-0.5436` n `7`; equity avg `-0.945` n `47`; fx avg `0.0191` n `4`; index avg `-0.1838` n `6`; metal avg `-1.9626` n `7`; unknown avg `-1.4097` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2269`, n `323`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2205`, n `323`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1528`, n `323`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1431`, n `319`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1406`, n `323`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1405`, n `319`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.136`, n `323`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `323`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `323`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `319`, weak_sample_signal
