# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T02:11:00.305117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5644` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.0089` n `230`; crypto_major avg `-0.5351` n `8`; equity avg `0.1281` n `121`; fx avg `-0.0049` n `6`; index avg `0.0213` n `25`; metal avg `0.0117` n `20`; unknown avg `0.2918` n `793`
- 1h: commodity avg `0.0712` n `12`; crypto_alt avg `0.5529` n `230`; crypto_major avg `0.7205` n `8`; equity avg `0.5606` n `121`; fx avg `-0.0768` n `6`; index avg `0.102` n `25`; metal avg `0.1024` n `20`; unknown avg `0.2399` n `793`
- 4h: commodity avg `0.0986` n `12`; crypto_alt avg `1.0541` n `230`; crypto_major avg `1.7608` n `8`; equity avg `0.8493` n `121`; fx avg `-0.1139` n `6`; index avg `0.1223` n `25`; metal avg `0.1964` n `20`; unknown avg `-0.2369` n `793`
- 24h: commodity avg `0.3757` n `12`; crypto_alt avg `5.0189` n `230`; crypto_major avg `6.5675` n `8`; equity avg `-0.6449` n `121`; fx avg `-0.0438` n `6`; index avg `-0.1519` n `25`; metal avg `0.4173` n `20`; unknown avg `2.6189` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
