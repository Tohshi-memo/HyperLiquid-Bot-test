# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T08:30:22.139726+00:00`
- Correlation status: `ready`
- Asset price records: `153`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `7`; crypto_alt avg `0.0216` n `223`; crypto_major avg `0.0228` n `7`; equity avg `-0.0046` n `42`; fx avg `-0.0021` n `4`; index avg `0.0001` n `9`; metal avg `0.002` n `7`; unknown avg `0.1126` n `313`
- 1h: commodity avg `-0.0065` n `7`; crypto_alt avg `0.1263` n `223`; crypto_major avg `-0.0554` n `7`; equity avg `0.0213` n `42`; fx avg `0.009` n `4`; index avg `-0.0192` n `9`; metal avg `0.0421` n `7`; unknown avg `-0.137` n `313`
- 4h: commodity avg `-0.0683` n `7`; crypto_alt avg `0.5858` n `223`; crypto_major avg `0.1404` n `7`; equity avg `-0.1803` n `42`; fx avg `0.0196` n `4`; index avg `0.0743` n `9`; metal avg `0.0938` n `7`; unknown avg `0.2135` n `311`
- 24h: commodity avg `-0.2124` n `7`; crypto_alt avg `1.5263` n `223`; crypto_major avg `-0.1755` n `7`; equity avg `0.177` n `42`; fx avg `0.1252` n `4`; index avg `0.0735` n `9`; metal avg `0.1029` n `7`; unknown avg `0.1009` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4249`, n `149`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4102`, n `149`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4036`, n `149`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3885`, n `145`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3858`, n `149`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3832`, n `145`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3755`, n `145`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.368`, n `145`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3589`, n `149`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3558`, n `149`, moderate_sample_signal
