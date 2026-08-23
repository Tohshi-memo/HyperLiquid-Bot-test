# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T23:52:23.457300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `0.0405` n `231`; crypto_major avg `-0.0602` n `8`; equity avg `0.0034` n `122`; fx avg `0.0071` n `6`; index avg `-0.0178` n `25`; metal avg `0.0159` n `20`; unknown avg `0.0954` n `793`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.1222` n `231`; crypto_major avg `-0.0135` n `8`; equity avg `0.1711` n `122`; fx avg `0.0021` n `6`; index avg `0.0121` n `25`; metal avg `0.0719` n `20`; unknown avg `1.1406` n `793`
- 4h: commodity avg `-0.1227` n `12`; crypto_alt avg `0.1192` n `231`; crypto_major avg `0.6318` n `8`; equity avg `0.125` n `122`; fx avg `-0.0209` n `6`; index avg `-0.0019` n `25`; metal avg `0.0334` n `20`; unknown avg `1.7761` n `793`
- 24h: commodity avg `-0.2464` n `12`; crypto_alt avg `3.3391` n `231`; crypto_major avg `1.6046` n `8`; equity avg `0.8349` n `122`; fx avg `-0.1059` n `6`; index avg `0.1194` n `25`; metal avg `0.1176` n `20`; unknown avg `5.826` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
