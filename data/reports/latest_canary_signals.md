# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T07:44:18.689288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1239` n `12`; crypto_alt avg `0.048` n `228`; crypto_major avg `-0.0281` n `8`; equity avg `-0.0448` n `67`; fx avg `-0.0014` n `6`; index avg `0.0108` n `23`; metal avg `0.0307` n `18`; unknown avg `0.2492` n `396`
- 1h: commodity avg `0.262` n `12`; crypto_alt avg `0.214` n `228`; crypto_major avg `0.1979` n `8`; equity avg `0.1004` n `67`; fx avg `0.0042` n `6`; index avg `0.0708` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.1861` n `396`
- 4h: commodity avg `0.1575` n `12`; crypto_alt avg `-0.0244` n `228`; crypto_major avg `0.2708` n `8`; equity avg `0.0847` n `67`; fx avg `0.0106` n `6`; index avg `0.0269` n `23`; metal avg `-0.0178` n `18`; unknown avg `-0.1158` n `386`
- 24h: commodity avg `-2.7534` n `12`; crypto_alt avg `2.4872` n `228`; crypto_major avg `3.1336` n `8`; equity avg `2.3939` n `67`; fx avg `0.0301` n `6`; index avg `1.3564` n `23`; metal avg `1.1275` n `18`; unknown avg `1.8223` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
