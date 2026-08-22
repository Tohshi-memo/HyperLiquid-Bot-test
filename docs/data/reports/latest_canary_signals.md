# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T21:07:27.085012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `-0.8273` n `230`; crypto_major avg `-0.6448` n `8`; equity avg `-0.0274` n `121`; fx avg `-0.008` n `6`; index avg `-0.0029` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.0392` n `794`
- 1h: commodity avg `0.0675` n `12`; crypto_alt avg `-0.9475` n `230`; crypto_major avg `-0.5427` n `8`; equity avg `0.0085` n `121`; fx avg `0.0112` n `6`; index avg `-0.003` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0311` n `794`
- 4h: commodity avg `0.0651` n `12`; crypto_alt avg `-0.7698` n `230`; crypto_major avg `0.3797` n `8`; equity avg `0.1109` n `121`; fx avg `0.022` n `6`; index avg `-0.0077` n `25`; metal avg `0.0034` n `20`; unknown avg `1.262` n `794`
- 24h: commodity avg `0.0402` n `12`; crypto_alt avg `-0.5158` n `230`; crypto_major avg `2.6509` n `8`; equity avg `-0.3821` n `121`; fx avg `0.0745` n `6`; index avg `-0.0433` n `25`; metal avg `-0.0806` n `20`; unknown avg `3.2346` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
