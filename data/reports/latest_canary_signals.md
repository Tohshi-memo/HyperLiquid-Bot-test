# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T11:45:24.501433+00:00`
- Correlation status: `ready`
- Asset price records: `262`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `7`; crypto_alt avg `0.0853` n `223`; crypto_major avg `-0.0305` n `7`; equity avg `-0.0581` n `42`; fx avg `0.0029` n `4`; index avg `-0.0189` n `9`; metal avg `-0.1078` n `7`; unknown avg `-0.0275` n `314`
- 1h: commodity avg `-0.0364` n `7`; crypto_alt avg `-0.143` n `223`; crypto_major avg `-0.2777` n `7`; equity avg `0.1497` n `42`; fx avg `-0.0097` n `4`; index avg `0.0239` n `9`; metal avg `-0.1977` n `7`; unknown avg `-0.0733` n `314`
- 4h: commodity avg `0.4576` n `7`; crypto_alt avg `-1.0001` n `223`; crypto_major avg `-1.3651` n `7`; equity avg `-0.7573` n `42`; fx avg `0.0038` n `4`; index avg `-0.4138` n `9`; metal avg `-1.0487` n `7`; unknown avg `0.0682` n `314`
- 24h: commodity avg `0.9995` n `7`; crypto_alt avg `0.893` n `223`; crypto_major avg `0.4698` n `7`; equity avg `0.2584` n `42`; fx avg `-0.0674` n `4`; index avg `0.4012` n `9`; metal avg `-1.8172` n `7`; unknown avg `-0.227` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2804`, n `258`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2726`, n `258`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1851`, n `258`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.182`, n `254`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.181`, n `254`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1797`, n `254`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1723`, n `258`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1702`, n `254`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1629`, n `258`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.161`, n `254`, weak_sample_signal
