# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T14:14:51.851755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.0141` n `230`; crypto_major avg `0.1055` n `8`; equity avg `-0.0626` n `92`; fx avg `0.0111` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0138` n `20`; unknown avg `-0.0173` n `765`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `0.1454` n `230`; crypto_major avg `0.2133` n `8`; equity avg `-0.0326` n `92`; fx avg `0.0122` n `6`; index avg `0.0004` n `25`; metal avg `-0.0109` n `20`; unknown avg `-0.0147` n `765`
- 4h: commodity avg `0.0094` n `12`; crypto_alt avg `0.4841` n `230`; crypto_major avg `0.448` n `8`; equity avg `-0.1202` n `92`; fx avg `0.0055` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0241` n `20`; unknown avg `-0.1612` n `765`
- 24h: commodity avg `0.1498` n `12`; crypto_alt avg `0.5269` n `229`; crypto_major avg `0.0292` n `8`; equity avg `0.0873` n `92`; fx avg `-0.0082` n `6`; index avg `0.0967` n `25`; metal avg `0.0416` n `20`; unknown avg `2.9704` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
