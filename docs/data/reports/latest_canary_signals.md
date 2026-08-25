# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T05:52:25.221299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6879` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.107` n `12`; crypto_alt avg `-0.0835` n `231`; crypto_major avg `-0.0444` n `8`; equity avg `-0.0347` n `122`; fx avg `0.0133` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0722` n `20`; unknown avg `-0.0142` n `794`
- 1h: commodity avg `-0.1223` n `12`; crypto_alt avg `0.3969` n `231`; crypto_major avg `0.5086` n `8`; equity avg `0.3579` n `122`; fx avg `0.0326` n `6`; index avg `0.0495` n `25`; metal avg `0.0585` n `20`; unknown avg `0.046` n `794`
- 4h: commodity avg `-0.209` n `12`; crypto_alt avg `1.2941` n `231`; crypto_major avg `1.3679` n `8`; equity avg `0.9384` n `122`; fx avg `0.0145` n `6`; index avg `0.1412` n `25`; metal avg `-0.32` n `20`; unknown avg `1.0143` n `794`
- 24h: commodity avg `-0.1842` n `12`; crypto_alt avg `2.092` n `231`; crypto_major avg `3.1722` n `8`; equity avg `0.1697` n `122`; fx avg `0.049` n `6`; index avg `0.0018` n `25`; metal avg `-0.173` n `20`; unknown avg `0.59` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
