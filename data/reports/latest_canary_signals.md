# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T09:00:09.654237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0965` n `231`; crypto_major avg `-0.0626` n `8`; equity avg `-0.0949` n `122`; fx avg `-0.0113` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0205` n `20`; unknown avg `0.0927` n `793`
- 1h: commodity avg `-0.1087` n `12`; crypto_alt avg `-0.52` n `231`; crypto_major avg `-0.5324` n `8`; equity avg `0.0634` n `122`; fx avg `-0.0209` n `6`; index avg `0.0258` n `25`; metal avg `-0.0825` n `20`; unknown avg `0.3062` n `793`
- 4h: commodity avg `0.0086` n `12`; crypto_alt avg `-0.3352` n `231`; crypto_major avg `-0.4191` n `8`; equity avg `-0.2611` n `122`; fx avg `0.029` n `6`; index avg `-0.0494` n `25`; metal avg `-0.0565` n `20`; unknown avg `0.2291` n `777`
- 24h: commodity avg `-0.2672` n `12`; crypto_alt avg `1.5556` n `231`; crypto_major avg `0.0392` n `8`; equity avg `-1.2958` n `122`; fx avg `-0.1396` n `6`; index avg `-0.1142` n `25`; metal avg `0.0912` n `20`; unknown avg `5.3259` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
