# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T17:28:54.355701+00:00`
- Correlation status: `ready`
- Asset price records: `92`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0362` n `7`; crypto_alt avg `-0.1574` n `223`; crypto_major avg `-0.1119` n `7`; equity avg `-0.0436` n `42`; fx avg `-0.0011` n `4`; index avg `0.0048` n `9`; metal avg `0.0047` n `7`; unknown avg `-0.0068` n `313`
- 1h: commodity avg `-0.0505` n `7`; crypto_alt avg `0.1378` n `223`; crypto_major avg `-0.0474` n `7`; equity avg `-0.0515` n `42`; fx avg `0.0359` n `4`; index avg `0.0047` n `9`; metal avg `0.0087` n `7`; unknown avg `0.1224` n `313`
- 4h: commodity avg `-0.0706` n `7`; crypto_alt avg `1.2735` n `223`; crypto_major avg `0.1823` n `7`; equity avg `-0.0304` n `42`; fx avg `0.0826` n `4`; index avg `-0.0014` n `9`; metal avg `-0.0132` n `7`; unknown avg `0.1205` n `313`
- 24h: commodity avg `0.5752` n `7`; crypto_alt avg `1.3468` n `223`; crypto_major avg `0.1102` n `7`; equity avg `0.2822` n `42`; fx avg `-0.0508` n `4`; index avg `0.1907` n `9`; metal avg `-0.6555` n `7`; unknown avg `0.6293` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5268`, n `88`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5243`, n `84`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5084`, n `88`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4986`, n `84`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4699`, n `84`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4655`, n `84`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4572`, n `84`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4521`, n `88`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4273`, n `88`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4238`, n `84`, moderate_sample_signal
