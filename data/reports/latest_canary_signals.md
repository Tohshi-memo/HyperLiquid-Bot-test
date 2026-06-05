# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T23:52:21.888303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.5634` n `228`; crypto_major avg `0.4354` n `8`; equity avg `0.0026` n `74`; fx avg `0.0` n `6`; index avg `0.0202` n `23`; metal avg `-0.0382` n `18`; unknown avg `-0.0326` n `425`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `-1.0362` n `228`; crypto_major avg `-0.975` n `8`; equity avg `-0.4306` n `74`; fx avg `0.0011` n `6`; index avg `-0.0708` n `23`; metal avg `-0.1863` n `18`; unknown avg `-0.1838` n `425`
- 4h: commodity avg `0.1086` n `12`; crypto_alt avg `0.4979` n `228`; crypto_major avg `0.3437` n `8`; equity avg `-0.8133` n `74`; fx avg `0.0026` n `6`; index avg `-0.265` n `23`; metal avg `-0.2085` n `18`; unknown avg `0.1421` n `425`
- 24h: commodity avg `-1.5233` n `12`; crypto_alt avg `-6.8599` n `228`; crypto_major avg `-6.2361` n `8`; equity avg `-6.1709` n `74`; fx avg `-0.0526` n `6`; index avg `-4.0653` n `23`; metal avg `-4.5331` n `18`; unknown avg `-0.441` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
