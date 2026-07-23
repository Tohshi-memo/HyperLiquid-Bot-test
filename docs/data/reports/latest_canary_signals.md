# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T16:37:35.839322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0782` n `12`; crypto_alt avg `0.1153` n `230`; crypto_major avg `0.0341` n `8`; equity avg `0.1911` n `100`; fx avg `-0.0042` n `6`; index avg `0.0244` n `25`; metal avg `-0.0233` n `20`; unknown avg `0.1156` n `772`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `-0.2306` n `8`; equity avg `0.8511` n `100`; fx avg `0.0028` n `6`; index avg `0.1596` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.0067` n `772`
- 4h: commodity avg `0.1054` n `12`; crypto_alt avg `-0.4066` n `230`; crypto_major avg `-0.9604` n `8`; equity avg `0.2259` n `100`; fx avg `-0.0304` n `6`; index avg `-0.0414` n `25`; metal avg `-0.1818` n `20`; unknown avg `-0.1388` n `772`
- 24h: commodity avg `1.0564` n `12`; crypto_alt avg `-1.5853` n `230`; crypto_major avg `-2.2884` n `8`; equity avg `-1.3058` n `99`; fx avg `-0.0747` n `6`; index avg `-0.3326` n `25`; metal avg `-0.8598` n `20`; unknown avg `-0.2302` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0648`, n `666`, weak_sample_signal
