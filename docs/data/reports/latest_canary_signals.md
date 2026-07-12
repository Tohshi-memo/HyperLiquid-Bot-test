# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T04:04:08.504703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `0.0358` n `230`; crypto_major avg `0.0591` n `8`; equity avg `-0.0127` n `92`; fx avg `0.0` n `6`; index avg `0.0105` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.1632` n `765`
- 1h: commodity avg `-0.0629` n `12`; crypto_alt avg `0.3604` n `230`; crypto_major avg `0.235` n `8`; equity avg `0.0188` n `92`; fx avg `-0.0031` n `6`; index avg `0.0045` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.4796` n `765`
- 4h: commodity avg `-0.1342` n `12`; crypto_alt avg `1.1727` n `230`; crypto_major avg `0.7571` n `8`; equity avg `0.0935` n `92`; fx avg `-0.0028` n `6`; index avg `-0.0378` n `25`; metal avg `-0.0202` n `20`; unknown avg `0.2949` n `765`
- 24h: commodity avg `0.3843` n `12`; crypto_alt avg `-0.3015` n `229`; crypto_major avg `-0.1394` n `8`; equity avg `0.1037` n `92`; fx avg `0.0177` n `6`; index avg `-0.0973` n `25`; metal avg `-0.0838` n `20`; unknown avg `-0.0243` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
