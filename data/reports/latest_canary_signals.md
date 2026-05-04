# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T23:45:32.426188+00:00`
- Correlation status: `ready`
- Asset price records: `309`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `7`; crypto_alt avg `-0.216` n `223`; crypto_major avg `-0.2173` n `7`; equity avg `-0.0886` n `47`; fx avg `-0.0021` n `4`; index avg `0.0016` n `6`; metal avg `-0.048` n `7`; unknown avg `-0.0146` n `312`
- 1h: commodity avg `0.0396` n `7`; crypto_alt avg `-0.3788` n `223`; crypto_major avg `-0.3122` n `7`; equity avg `-0.2333` n `47`; fx avg `0.0021` n `4`; index avg `-0.0064` n `6`; metal avg `-0.0576` n `7`; unknown avg `-0.0431` n `312`
- 4h: commodity avg `-0.041` n `7`; crypto_alt avg `-0.2303` n `223`; crypto_major avg `-0.1861` n `7`; equity avg `-0.3519` n `47`; fx avg `0.0119` n `4`; index avg `-0.0597` n `6`; metal avg `-0.1337` n `7`; unknown avg `-0.1185` n `312`
- 24h: commodity avg `1.3699` n `7`; crypto_alt avg `1.718` n `223`; crypto_major avg `0.8652` n `7`; equity avg `-0.2483` n `47`; fx avg `-0.0132` n `4`; index avg `-0.007` n `6`; metal avg `-2.348` n `7`; unknown avg `-1.2523` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.236`, n `305`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2302`, n `305`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1891`, n `301`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1871`, n `301`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `305`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `305`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1417`, n `305`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `305`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1207`, n `305`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `301`, weak_sample_signal
