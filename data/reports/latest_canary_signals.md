# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T01:22:27.738290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0582` n `12`; crypto_alt avg `-0.1319` n `230`; crypto_major avg `-0.2131` n `8`; equity avg `-0.0307` n `92`; fx avg `-0.0054` n `6`; index avg `-0.0224` n `25`; metal avg `-0.048` n `20`; unknown avg `0.0633` n `766`
- 1h: commodity avg `0.113` n `12`; crypto_alt avg `-0.6615` n `230`; crypto_major avg `-0.7304` n `8`; equity avg `-0.9262` n `92`; fx avg `0.0168` n `6`; index avg `-0.2163` n `25`; metal avg `-0.1301` n `20`; unknown avg `0.4857` n `766`
- 4h: commodity avg `-0.0632` n `12`; crypto_alt avg `-0.419` n `230`; crypto_major avg `-0.2818` n `8`; equity avg `-1.1289` n `92`; fx avg `0.0461` n `6`; index avg `-0.2829` n `25`; metal avg `-0.2642` n `20`; unknown avg `-0.0473` n `765`
- 24h: commodity avg `0.1079` n `12`; crypto_alt avg `-0.4523` n `230`; crypto_major avg `0.2205` n `8`; equity avg `-1.0912` n `92`; fx avg `-0.0079` n `6`; index avg `-0.2663` n `25`; metal avg `-0.3193` n `20`; unknown avg `0.3069` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
