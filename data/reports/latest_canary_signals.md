# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T06:30:26.369106+00:00`
- Correlation status: `ready`
- Asset price records: `145`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `7`; crypto_alt avg `-0.0222` n `223`; crypto_major avg `-0.0767` n `7`; equity avg `-0.0587` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0005` n `9`; metal avg `0.004` n `7`; unknown avg `-0.056` n `313`
- 1h: commodity avg `-0.0605` n `7`; crypto_alt avg `-0.1364` n `223`; crypto_major avg `-0.2243` n `7`; equity avg `0.0416` n `42`; fx avg `0.0027` n `4`; index avg `0.0378` n `9`; metal avg `0.0039` n `7`; unknown avg `-0.2329` n `311`
- 4h: commodity avg `-0.0095` n `7`; crypto_alt avg `0.1634` n `223`; crypto_major avg `0.0261` n `7`; equity avg `-0.0218` n `42`; fx avg `0.004` n `4`; index avg `0.0059` n `9`; metal avg `0.0342` n `7`; unknown avg `-0.0326` n `311`
- 24h: commodity avg `-0.1785` n `7`; crypto_alt avg `1.144` n `223`; crypto_major avg `-0.1198` n `7`; equity avg `0.4996` n `42`; fx avg `0.1309` n `4`; index avg `0.0346` n `9`; metal avg `0.0643` n `7`; unknown avg `0.2921` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4412`, n `141`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4261`, n `141`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4044`, n `141`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3992`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3956`, n `137`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `141`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3863`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3802`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3613`, n `137`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.344`, n `137`, moderate_sample_signal
