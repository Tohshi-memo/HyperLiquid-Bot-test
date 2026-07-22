# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T02:22:24.478219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0626` n `12`; crypto_alt avg `0.1483` n `230`; crypto_major avg `0.1304` n `8`; equity avg `-0.0265` n `98`; fx avg `0.0088` n `6`; index avg `0.0078` n `25`; metal avg `-0.0159` n `20`; unknown avg `-0.0242` n `771`
- 1h: commodity avg `-0.0442` n `11`; crypto_alt avg `0.1422` n `230`; crypto_major avg `0.0917` n `8`; equity avg `-0.3485` n `87`; fx avg `0.0099` n `5`; index avg `-0.0016` n `19`; metal avg `0.0946` n `16`; unknown avg `0.0596` n `754`
- 4h: commodity avg `0.1218` n `12`; crypto_alt avg `0.1873` n `230`; crypto_major avg `0.3102` n `8`; equity avg `-0.0753` n `98`; fx avg `0.0163` n `6`; index avg `0.0325` n `25`; metal avg `0.4325` n `20`; unknown avg `-0.0869` n `771`
- 24h: commodity avg `0.6387` n `12`; crypto_alt avg `1.029` n `230`; crypto_major avg `0.8682` n `8`; equity avg `4.2167` n `98`; fx avg `0.0206` n `6`; index avg `0.5879` n `25`; metal avg `1.0693` n `20`; unknown avg `0.4128` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0966`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0589`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
