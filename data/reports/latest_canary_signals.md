# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T15:52:24.835458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.0874` n `231`; crypto_major avg `-0.0361` n `8`; equity avg `0.0097` n `122`; fx avg `0.0001` n `6`; index avg `-0.0013` n `25`; metal avg `0.0168` n `20`; unknown avg `0.1134` n `793`
- 1h: commodity avg `-0.0053` n `12`; crypto_alt avg `0.9018` n `231`; crypto_major avg `0.0335` n `8`; equity avg `0.1175` n `122`; fx avg `0.0008` n `6`; index avg `0.0118` n `25`; metal avg `0.0355` n `20`; unknown avg `0.283` n `793`
- 4h: commodity avg `-0.0095` n `12`; crypto_alt avg `1.9266` n `231`; crypto_major avg `0.0695` n `8`; equity avg `0.1735` n `122`; fx avg `0.0024` n `6`; index avg `0.0261` n `25`; metal avg `0.0368` n `20`; unknown avg `2.6628` n `793`
- 24h: commodity avg `0.0459` n `12`; crypto_alt avg `3.0616` n `231`; crypto_major avg `1.8984` n `8`; equity avg `0.6802` n `122`; fx avg `0.0384` n `6`; index avg `0.0617` n `25`; metal avg `0.0775` n `20`; unknown avg `8.5334` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
