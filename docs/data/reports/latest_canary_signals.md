# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T02:37:28.576127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.1229` n `230`; crypto_major avg `-0.1966` n `8`; equity avg `-0.1523` n `98`; fx avg `-0.0024` n `6`; index avg `-0.0242` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.0358` n `771`
- 1h: commodity avg `-0.1072` n `12`; crypto_alt avg `0.0399` n `230`; crypto_major avg `-0.162` n `8`; equity avg `-0.179` n `98`; fx avg `0.014` n `6`; index avg `-0.0322` n `25`; metal avg `0.0261` n `20`; unknown avg `0.0631` n `771`
- 4h: commodity avg `0.0641` n `12`; crypto_alt avg `0.1488` n `230`; crypto_major avg `0.0801` n `8`; equity avg `-0.1621` n `98`; fx avg `0.0139` n `6`; index avg `0.0138` n `25`; metal avg `0.4076` n `20`; unknown avg `-0.168` n `771`
- 24h: commodity avg `0.575` n `12`; crypto_alt avg `0.7532` n `230`; crypto_major avg `0.4547` n `8`; equity avg `3.7012` n `98`; fx avg `0.016` n `6`; index avg `0.4837` n `25`; metal avg `0.9185` n `20`; unknown avg `0.3715` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0598`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
