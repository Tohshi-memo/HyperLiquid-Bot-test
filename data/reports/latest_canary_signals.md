# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T08:07:29.566159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0358` n `12`; crypto_alt avg `0.0262` n `229`; crypto_major avg `0.1464` n `8`; equity avg `0.1606` n `88`; fx avg `-0.0031` n `6`; index avg `0.0215` n `25`; metal avg `0.0147` n `20`; unknown avg `0.0548` n `765`
- 1h: commodity avg `-0.1795` n `12`; crypto_alt avg `0.3383` n `229`; crypto_major avg `0.3968` n `8`; equity avg `0.1609` n `88`; fx avg `-0.0087` n `6`; index avg `0.0443` n `25`; metal avg `0.2884` n `20`; unknown avg `0.0931` n `765`
- 4h: commodity avg `-0.0392` n `12`; crypto_alt avg `-0.4446` n `229`; crypto_major avg `-0.0963` n `8`; equity avg `0.498` n `88`; fx avg `0.0102` n `6`; index avg `0.1948` n `25`; metal avg `0.2531` n `20`; unknown avg `-0.1412` n `731`
- 24h: commodity avg `-0.2705` n `12`; crypto_alt avg `-0.0942` n `229`; crypto_major avg `1.0355` n `8`; equity avg `-0.4535` n `88`; fx avg `0.0764` n `6`; index avg `0.0203` n `25`; metal avg `0.0081` n `20`; unknown avg `1.2067` n `661`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
