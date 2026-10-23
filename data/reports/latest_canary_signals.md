# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T06:22:26.434000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `0.2578` n `237`; crypto_major avg `0.2374` n `8`; equity avg `0.4476` n `151`; fx avg `0.002` n `6`; index avg `0.071` n `26`; metal avg `0.0271` n `20`; unknown avg `1.2844` n `1234`
- 1h: commodity avg `0.0638` n `13`; crypto_alt avg `0.2903` n `237`; crypto_major avg `0.3202` n `8`; equity avg `0.7696` n `151`; fx avg `0.0091` n `6`; index avg `0.1042` n `26`; metal avg `0.0754` n `20`; unknown avg `0.7772` n `1211`
- 4h: commodity avg `0.0139` n `13`; crypto_alt avg `0.8198` n `237`; crypto_major avg `0.5792` n `8`; equity avg `1.7334` n `151`; fx avg `0.0173` n `6`; index avg `0.2323` n `26`; metal avg `0.1093` n `20`; unknown avg `3.6616` n `1203`
- 24h: commodity avg `0.2635` n `13`; crypto_alt avg `-0.4186` n `237`; crypto_major avg `-0.3938` n `8`; equity avg `-1.3221` n `151`; fx avg `-0.0795` n `6`; index avg `-0.0898` n `26`; metal avg `-0.5283` n `20`; unknown avg `52.3803` n `899`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
