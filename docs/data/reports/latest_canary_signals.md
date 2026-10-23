# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T19:37:38.423227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0608` n `13`; crypto_alt avg `0.1932` n `237`; crypto_major avg `0.1554` n `8`; equity avg `-0.1025` n `152`; fx avg `0.0014` n `6`; index avg `0.0026` n `26`; metal avg `0.0059` n `20`; unknown avg `193.1756` n `1228`
- 1h: commodity avg `0.1388` n `13`; crypto_alt avg `-0.6993` n `237`; crypto_major avg `-0.3921` n `8`; equity avg `-0.2725` n `152`; fx avg `0.001` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0257` n `20`; unknown avg `92.8561` n `1228`
- 4h: commodity avg `0.192` n `13`; crypto_alt avg `-0.3069` n `237`; crypto_major avg `-0.4715` n `8`; equity avg `-0.4244` n `152`; fx avg `-0.0176` n `6`; index avg `-0.0522` n `26`; metal avg `-0.0616` n `20`; unknown avg `6.3863` n `1195`
- 24h: commodity avg `0.3959` n `13`; crypto_alt avg `0.4572` n `237`; crypto_major avg `0.1937` n `8`; equity avg `1.3341` n `152`; fx avg `-0.0868` n `6`; index avg `0.107` n `26`; metal avg `-0.0879` n `20`; unknown avg `0.8515` n `1034`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
