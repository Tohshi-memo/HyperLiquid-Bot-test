# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T19:37:28.788127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1188` n `12`; crypto_alt avg `-0.1773` n `228`; crypto_major avg `-0.1346` n `8`; equity avg `0.07` n `74`; fx avg `0.0058` n `6`; index avg `0.043` n `23`; metal avg `0.0267` n `18`; unknown avg `0.0182` n `517`
- 1h: commodity avg `0.111` n `12`; crypto_alt avg `0.0484` n `228`; crypto_major avg `0.222` n `8`; equity avg `-0.3889` n `74`; fx avg `-0.0196` n `6`; index avg `-0.2765` n `23`; metal avg `-0.0923` n `18`; unknown avg `-0.0188` n `517`
- 4h: commodity avg `0.0599` n `12`; crypto_alt avg `0.167` n `228`; crypto_major avg `-0.0771` n `8`; equity avg `-0.5445` n `74`; fx avg `-0.0324` n `6`; index avg `-0.4746` n `23`; metal avg `-0.1495` n `18`; unknown avg `-0.1651` n `517`
- 24h: commodity avg `-0.9597` n `12`; crypto_alt avg `4.479` n `228`; crypto_major avg `4.7331` n `8`; equity avg `2.5976` n `74`; fx avg `-0.3125` n `6`; index avg `0.9329` n `23`; metal avg `0.0867` n `18`; unknown avg `-1.5269` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
