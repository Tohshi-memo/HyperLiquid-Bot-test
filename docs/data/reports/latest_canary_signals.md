# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T09:52:28.370141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `0.0903` n `230`; crypto_major avg `0.0265` n `8`; equity avg `-0.0085` n `98`; fx avg `0.0083` n `6`; index avg `0.0159` n `25`; metal avg `0.0116` n `20`; unknown avg `0.0002` n `771`
- 1h: commodity avg `0.2057` n `12`; crypto_alt avg `-0.0023` n `230`; crypto_major avg `0.1126` n `8`; equity avg `0.0216` n `98`; fx avg `0.0025` n `6`; index avg `0.0322` n `25`; metal avg `0.0185` n `20`; unknown avg `0.0116` n `771`
- 4h: commodity avg `0.3289` n `12`; crypto_alt avg `0.0478` n `230`; crypto_major avg `0.428` n `8`; equity avg `0.6702` n `98`; fx avg `0.0492` n `6`; index avg `0.0744` n `25`; metal avg `0.2109` n `20`; unknown avg `-0.0053` n `755`
- 24h: commodity avg `0.508` n `12`; crypto_alt avg `2.3145` n `230`; crypto_major avg `2.7554` n `8`; equity avg `1.6154` n `98`; fx avg `-0.067` n `6`; index avg `0.2306` n `25`; metal avg `0.5723` n `20`; unknown avg `0.1734` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
