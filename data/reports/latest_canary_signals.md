# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T22:52:26.572383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.0763` n `231`; crypto_major avg `0.1207` n `8`; equity avg `0.0326` n `122`; fx avg `-0.008` n `6`; index avg `0.031` n `25`; metal avg `-0.0429` n `20`; unknown avg `-0.1089` n `793`
- 1h: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.295` n `231`; crypto_major avg `-0.077` n `8`; equity avg `-0.0552` n `122`; fx avg `0.011` n `6`; index avg `-0.0125` n `25`; metal avg `-0.049` n `20`; unknown avg `-0.1749` n `793`
- 4h: commodity avg `-0.0879` n `12`; crypto_alt avg `0.3501` n `231`; crypto_major avg `0.7677` n `8`; equity avg `0.0214` n `122`; fx avg `-0.0929` n `6`; index avg `-0.009` n `25`; metal avg `-0.0357` n `20`; unknown avg `0.7119` n `793`
- 24h: commodity avg `-0.223` n `12`; crypto_alt avg `3.7382` n `231`; crypto_major avg `2.0697` n `8`; equity avg `0.7436` n `122`; fx avg `-0.0987` n `6`; index avg `0.1161` n `25`; metal avg `0.0647` n `20`; unknown avg `5.556` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
