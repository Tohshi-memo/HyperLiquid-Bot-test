# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T09:15:38.323978+00:00`
- Correlation status: `ready`
- Asset price records: `156`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `7`; crypto_alt avg `-0.0554` n `223`; crypto_major avg `0.0995` n `7`; equity avg `0.0143` n `42`; fx avg `-0.0043` n `4`; index avg `-0.0053` n `9`; metal avg `0.0167` n `7`; unknown avg `0.0542` n `313`
- 1h: commodity avg `0.0077` n `7`; crypto_alt avg `-0.0837` n `223`; crypto_major avg `0.1897` n `7`; equity avg `-0.103` n `42`; fx avg `-0.0053` n `4`; index avg `-0.0518` n `9`; metal avg `0.0268` n `7`; unknown avg `0.2967` n `313`
- 4h: commodity avg `-0.0668` n `7`; crypto_alt avg `0.3077` n `223`; crypto_major avg `0.2853` n `7`; equity avg `-0.1595` n `42`; fx avg `0.0191` n `4`; index avg `0.022` n `9`; metal avg `0.119` n `7`; unknown avg `0.1389` n `311`
- 24h: commodity avg `-0.2097` n `7`; crypto_alt avg `1.0564` n `223`; crypto_major avg `-0.1544` n `7`; equity avg `0.2012` n `42`; fx avg `0.1172` n `4`; index avg `0.0333` n `9`; metal avg `0.1181` n `7`; unknown avg `0.2045` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.422`, n `152`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4072`, n `152`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4033`, n `152`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3888`, n `148`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3855`, n `152`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3835`, n `148`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3762`, n `148`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3687`, n `148`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3397`, n `152`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3384`, n `152`, moderate_sample_signal
