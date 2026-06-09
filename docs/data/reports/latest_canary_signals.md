# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T06:37:26.451817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.126` n `12`; crypto_alt avg `-0.1579` n `228`; crypto_major avg `-0.1604` n `8`; equity avg `-0.0725` n `74`; fx avg `0.0215` n `6`; index avg `-0.0722` n `23`; metal avg `-0.1731` n `18`; unknown avg `0.0212` n `547`
- 1h: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.0802` n `228`; crypto_major avg `-0.1409` n `8`; equity avg `0.1294` n `74`; fx avg `0.0327` n `6`; index avg `-0.0215` n `23`; metal avg `-0.0502` n `18`; unknown avg `0.0772` n `503`
- 4h: commodity avg `-0.2293` n `12`; crypto_alt avg `1.8968` n `228`; crypto_major avg `1.4568` n `8`; equity avg `1.2164` n `74`; fx avg `-0.0011` n `6`; index avg `0.5153` n `23`; metal avg `0.3331` n `18`; unknown avg `0.325` n `503`
- 24h: commodity avg `-1.5211` n `12`; crypto_alt avg `0.6193` n `228`; crypto_major avg `1.2036` n `8`; equity avg `3.2864` n `74`; fx avg `-0.1262` n `6`; index avg `1.397` n `23`; metal avg `0.8898` n `18`; unknown avg `-2.7925` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
