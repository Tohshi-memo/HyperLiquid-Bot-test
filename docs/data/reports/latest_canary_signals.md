# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T13:37:30.297116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0309` n `12`; crypto_alt avg `-0.1127` n `230`; crypto_major avg `-0.1111` n `8`; equity avg `0.2193` n `98`; fx avg `-0.0024` n `6`; index avg `0.0321` n `25`; metal avg `-0.0262` n `20`; unknown avg `-0.0145` n `771`
- 1h: commodity avg `0.0715` n `12`; crypto_alt avg `-0.1928` n `230`; crypto_major avg `-0.1247` n `8`; equity avg `0.4139` n `98`; fx avg `-0.0247` n `6`; index avg `0.0483` n `25`; metal avg `-0.1045` n `20`; unknown avg `0.0553` n `771`
- 4h: commodity avg `0.1696` n `12`; crypto_alt avg `-0.1289` n `230`; crypto_major avg `-0.2024` n `8`; equity avg `0.1425` n `98`; fx avg `-0.0312` n `6`; index avg `0.042` n `25`; metal avg `-0.1807` n `20`; unknown avg `0.0302` n `771`
- 24h: commodity avg `0.6107` n `12`; crypto_alt avg `1.532` n `230`; crypto_major avg `1.9642` n `8`; equity avg `1.2351` n `98`; fx avg `-0.0783` n `6`; index avg `0.1143` n `25`; metal avg `0.4771` n `20`; unknown avg `0.075` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0616`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0599`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0597`, n `666`, weak_sample_signal
