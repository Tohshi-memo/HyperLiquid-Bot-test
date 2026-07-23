# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T02:07:30.003280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.119` n `230`; crypto_major avg `-0.1119` n `8`; equity avg `-0.1609` n `98`; fx avg `0.0093` n `6`; index avg `-0.0255` n `25`; metal avg `-0.0111` n `20`; unknown avg `0.0441` n `773`
- 1h: commodity avg `0.0452` n `12`; crypto_alt avg `-0.3647` n `230`; crypto_major avg `-0.4044` n `8`; equity avg `-0.3565` n `98`; fx avg `-0.0332` n `6`; index avg `-0.0674` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.3755` n `773`
- 4h: commodity avg `0.0733` n `12`; crypto_alt avg `-0.4717` n `230`; crypto_major avg `-0.2605` n `8`; equity avg `0.1281` n `98`; fx avg `-0.0713` n `6`; index avg `0.0976` n `25`; metal avg `0.1017` n `20`; unknown avg `-0.0278` n `773`
- 24h: commodity avg `0.6059` n `12`; crypto_alt avg `-0.7378` n `230`; crypto_major avg `-0.8608` n `8`; equity avg `-0.8719` n `98`; fx avg `-0.1338` n `6`; index avg `-0.1082` n `25`; metal avg `-0.1693` n `20`; unknown avg `1.7356` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0745`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
