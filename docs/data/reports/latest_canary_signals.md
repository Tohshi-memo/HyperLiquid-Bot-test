# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T16:07:27.883105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.0338` n `230`; crypto_major avg `0.0138` n `8`; equity avg `0.0116` n `92`; fx avg `-0.0165` n `6`; index avg `0.0006` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0809` n `765`
- 1h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.3548` n `230`; crypto_major avg `-0.248` n `8`; equity avg `-0.067` n `92`; fx avg `-0.0249` n `6`; index avg `0.0015` n `25`; metal avg `0.0071` n `20`; unknown avg `0.1561` n `765`
- 4h: commodity avg `-0.0477` n `12`; crypto_alt avg `0.1463` n `230`; crypto_major avg `0.2599` n `8`; equity avg `-0.1187` n `92`; fx avg `-0.0335` n `6`; index avg `0.0113` n `25`; metal avg `-0.0169` n `20`; unknown avg `0.2108` n `765`
- 24h: commodity avg `0.1391` n `12`; crypto_alt avg `0.7824` n `229`; crypto_major avg `0.4917` n `8`; equity avg `0.2055` n `92`; fx avg `-0.0455` n `6`; index avg `0.0799` n `25`; metal avg `-0.0003` n `20`; unknown avg `2.9487` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
