# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T15:07:26.207850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.4423` n `231`; crypto_major avg `0.1181` n `8`; equity avg `0.0541` n `122`; fx avg `-0.0011` n `6`; index avg `0.0013` n `25`; metal avg `0.009` n `20`; unknown avg `0.1016` n `793`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.015` n `231`; crypto_major avg `-0.2935` n `8`; equity avg `0.007` n `122`; fx avg `0.0055` n `6`; index avg `0.0123` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.4195` n `793`
- 4h: commodity avg `-0.0023` n `12`; crypto_alt avg `2.184` n `231`; crypto_major avg `0.9355` n `8`; equity avg `0.1968` n `122`; fx avg `-0.0003` n `6`; index avg `0.0192` n `25`; metal avg `0.0304` n `20`; unknown avg `3.9277` n `793`
- 24h: commodity avg `0.0678` n `12`; crypto_alt avg `2.5231` n `231`; crypto_major avg `2.0036` n `8`; equity avg `0.5898` n `122`; fx avg `0.0523` n `6`; index avg `0.0616` n `25`; metal avg `0.0618` n `20`; unknown avg `8.5197` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
