# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T13:22:29.704251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1866` n `12`; crypto_alt avg `-0.5364` n `228`; crypto_major avg `-0.66` n `8`; equity avg `-0.1756` n `74`; fx avg `0.0025` n `6`; index avg `-0.1517` n `23`; metal avg `-0.2365` n `18`; unknown avg `-0.2117` n `547`
- 1h: commodity avg `-0.3269` n `12`; crypto_alt avg `-0.2393` n `228`; crypto_major avg `-0.589` n `8`; equity avg `-0.0619` n `74`; fx avg `0.0058` n `6`; index avg `-0.0925` n `23`; metal avg `-0.1135` n `18`; unknown avg `-0.2216` n `547`
- 4h: commodity avg `0.0093` n `12`; crypto_alt avg `-0.1008` n `228`; crypto_major avg `-1.0538` n `8`; equity avg `-0.0888` n `74`; fx avg `0.1299` n `6`; index avg `-0.0842` n `23`; metal avg `0.2459` n `18`; unknown avg `0.0116` n `547`
- 24h: commodity avg `-0.4595` n `12`; crypto_alt avg `-1.604` n `228`; crypto_major avg `-1.8112` n `8`; equity avg `0.6733` n `74`; fx avg `0.1317` n `6`; index avg `0.4186` n `23`; metal avg `0.3692` n `18`; unknown avg `-1.0719` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
