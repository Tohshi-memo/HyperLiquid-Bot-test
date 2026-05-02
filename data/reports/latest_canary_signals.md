# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T23:00:28.210177+00:00`
- Correlation status: `ready`
- Asset price records: `115`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0355` n `7`; crypto_alt avg `0.0196` n `223`; crypto_major avg `0.0711` n `7`; equity avg `-0.0125` n `42`; fx avg `0.0021` n `4`; index avg `-0.0053` n `9`; metal avg `0.0007` n `7`; unknown avg `-0.038` n `313`
- 1h: commodity avg `0.0692` n `7`; crypto_alt avg `-0.1589` n `223`; crypto_major avg `-0.0981` n `7`; equity avg `-0.1258` n `42`; fx avg `-0.0114` n `4`; index avg `-0.0129` n `9`; metal avg `0.0099` n `7`; unknown avg `-0.0341` n `313`
- 4h: commodity avg `0.0131` n `7`; crypto_alt avg `0.263` n `223`; crypto_major avg `0.1042` n `7`; equity avg `0.2811` n `42`; fx avg `0.0348` n `4`; index avg `-0.0059` n `9`; metal avg `0.0057` n `7`; unknown avg `0.0899` n `313`
- 24h: commodity avg `-0.1505` n `7`; crypto_alt avg `2.0822` n `223`; crypto_major avg `0.8785` n `7`; equity avg `0.703` n `42`; fx avg `0.0115` n `4`; index avg `-0.0387` n `9`; metal avg `0.0295` n `7`; unknown avg `0.321` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4885`, n `111`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4716`, n `111`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4621`, n `107`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4171`, n `107`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4171`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4152`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4132`, n `107`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4098`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `111`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3851`, n `111`, moderate_sample_signal
