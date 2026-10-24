# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T11:52:28.111572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0537` n `13`; crypto_alt avg `-0.0324` n `237`; crypto_major avg `-0.0013` n `8`; equity avg `0.0124` n `152`; fx avg `0.0013` n `6`; index avg `0.0006` n `26`; metal avg `0.0041` n `20`; unknown avg `0.8854` n `1230`
- 1h: commodity avg `0.0821` n `13`; crypto_alt avg `-0.0725` n `237`; crypto_major avg `0.0269` n `8`; equity avg `0.0154` n `152`; fx avg `-0.0144` n `6`; index avg `-0.0081` n `26`; metal avg `0.0001` n `20`; unknown avg `0.1362` n `1230`
- 4h: commodity avg `0.1017` n `13`; crypto_alt avg `-0.2692` n `237`; crypto_major avg `-0.5301` n `8`; equity avg `-0.1068` n `152`; fx avg `-0.0084` n `6`; index avg `-0.0291` n `26`; metal avg `-0.0304` n `20`; unknown avg `12.2112` n `1196`
- 24h: commodity avg `0.3695` n `13`; crypto_alt avg `-2.8686` n `237`; crypto_major avg `-2.2601` n `8`; equity avg `-0.5627` n `152`; fx avg `0.005` n `6`; index avg `-0.0292` n `26`; metal avg `-0.229` n `20`; unknown avg `193.8615` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
