# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T09:30:26.475170+00:00`
- Correlation status: `ready`
- Asset price records: `253`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1196` n `7`; crypto_alt avg `-0.056` n `223`; crypto_major avg `-0.0902` n `7`; equity avg `-0.0089` n `42`; fx avg `0.013` n `4`; index avg `-0.058` n `9`; metal avg `-0.0288` n `7`; unknown avg `-0.103` n `314`
- 1h: commodity avg `-0.105` n `7`; crypto_alt avg `0.0784` n `223`; crypto_major avg `0.0074` n `7`; equity avg `0.1019` n `42`; fx avg `0.0228` n `4`; index avg `-0.1915` n `9`; metal avg `0.0886` n `7`; unknown avg `-0.0099` n `314`
- 4h: commodity avg `0.5891` n `7`; crypto_alt avg `-0.0037` n `223`; crypto_major avg `-0.6219` n `7`; equity avg `-0.1443` n `42`; fx avg `0.0199` n `4`; index avg `-0.309` n `9`; metal avg `-0.8385` n `7`; unknown avg `0.0408` n `312`
- 24h: commodity avg `0.5569` n `7`; crypto_alt avg `2.056` n `223`; crypto_major avg `1.8076` n `7`; equity avg `1.0593` n `42`; fx avg `-0.0383` n `4`; index avg `0.607` n `9`; metal avg `-0.9271` n `7`; unknown avg `0.1695` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3351`, n `249`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3242`, n `249`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.264`, n `245`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2607`, n `245`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.218`, n `245`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2054`, n `245`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1927`, n `249`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1811`, n `245`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1784`, n `249`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `249`, weak_sample_signal
