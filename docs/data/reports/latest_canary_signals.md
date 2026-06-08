# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T13:37:26.971753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2193` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1219` n `12`; crypto_alt avg `-0.3384` n `228`; crypto_major avg `-0.4448` n `8`; equity avg `-0.9339` n `74`; fx avg `0.0027` n `6`; index avg `-0.0723` n `23`; metal avg `0.2126` n `18`; unknown avg `0.0412` n `517`
- 1h: commodity avg `-0.2563` n `12`; crypto_alt avg `0.1103` n `228`; crypto_major avg `0.3433` n `8`; equity avg `-0.6284` n `74`; fx avg `0.0312` n `6`; index avg `-0.0237` n `23`; metal avg `0.0033` n `18`; unknown avg `0.5312` n `517`
- 4h: commodity avg `-1.1268` n `12`; crypto_alt avg `1.2362` n `228`; crypto_major avg `1.0925` n `8`; equity avg `0.6346` n `74`; fx avg `0.0754` n `6`; index avg `0.7013` n `23`; metal avg `1.007` n `18`; unknown avg `-1.6148` n `517`
- 24h: commodity avg `-0.5977` n `12`; crypto_alt avg `2.6824` n `228`; crypto_major avg `3.9045` n `8`; equity avg `1.7314` n `74`; fx avg `-0.2779` n `6`; index avg `1.0944` n `23`; metal avg `0.4987` n `18`; unknown avg `-2.7764` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
