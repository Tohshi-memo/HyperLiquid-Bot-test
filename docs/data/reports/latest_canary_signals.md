# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T14:22:29.315817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.139` n `230`; crypto_major avg `-0.2362` n `8`; equity avg `0.0508` n `98`; fx avg `0.0119` n `6`; index avg `0.0503` n `25`; metal avg `0.0657` n `20`; unknown avg `-0.0593` n `771`
- 1h: commodity avg `0.0428` n `12`; crypto_alt avg `-0.0584` n `230`; crypto_major avg `-0.183` n `8`; equity avg `0.4233` n `98`; fx avg `0.0363` n `6`; index avg `0.0516` n `25`; metal avg `0.084` n `20`; unknown avg `-0.0282` n `771`
- 4h: commodity avg `0.194` n `12`; crypto_alt avg `-0.1528` n `230`; crypto_major avg `-0.2222` n `8`; equity avg `0.385` n `98`; fx avg `0.007` n `6`; index avg `0.0361` n `25`; metal avg `-0.1165` n `20`; unknown avg `0.0476` n `771`
- 24h: commodity avg `0.5069` n `12`; crypto_alt avg `2.356` n `230`; crypto_major avg `2.8086` n `8`; equity avg `2.7261` n `98`; fx avg `-0.0343` n `6`; index avg `0.3167` n `25`; metal avg `0.6871` n `20`; unknown avg `0.2351` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0862`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0564`, n `666`, weak_sample_signal
