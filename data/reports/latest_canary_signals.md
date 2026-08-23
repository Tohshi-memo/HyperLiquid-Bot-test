# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T17:37:26.146504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.0757` n `231`; crypto_major avg `-0.2367` n `8`; equity avg `0.0115` n `122`; fx avg `0.0021` n `6`; index avg `-0.0082` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0286` n `793`
- 1h: commodity avg `0.0192` n `12`; crypto_alt avg `0.3613` n `231`; crypto_major avg `0.0442` n `8`; equity avg `0.062` n `122`; fx avg `-0.0021` n `6`; index avg `0.007` n `25`; metal avg `-0.0115` n `20`; unknown avg `0.0412` n `793`
- 4h: commodity avg `-0.0115` n `12`; crypto_alt avg `0.8417` n `231`; crypto_major avg `-0.162` n `8`; equity avg `0.1527` n `122`; fx avg `-0.0009` n `6`; index avg `0.0259` n `25`; metal avg `0.022` n `20`; unknown avg `0.631` n `793`
- 24h: commodity avg `0.0305` n `12`; crypto_alt avg `2.1833` n `231`; crypto_major avg `0.9622` n `8`; equity avg `0.6976` n `122`; fx avg `0.0383` n `6`; index avg `0.0782` n `25`; metal avg `0.07` n `20`; unknown avg `7.8925` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
