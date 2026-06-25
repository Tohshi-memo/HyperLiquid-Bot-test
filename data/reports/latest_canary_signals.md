# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T23:52:27.821781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `-0.2195` n `228`; crypto_major avg `-0.4829` n `8`; equity avg `-0.2713` n `86`; fx avg `0.0187` n `6`; index avg `-0.0785` n `23`; metal avg `-0.0688` n `20`; unknown avg `0.2299` n `765`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `0.1681` n `228`; crypto_major avg `0.3135` n `8`; equity avg `0.1834` n `86`; fx avg `0.004` n `6`; index avg `0.0148` n `23`; metal avg `-0.0058` n `20`; unknown avg `0.3577` n `765`
- 4h: commodity avg `-0.0646` n `12`; crypto_alt avg `1.3167` n `228`; crypto_major avg `1.4184` n `8`; equity avg `0.1725` n `86`; fx avg `-0.0134` n `6`; index avg `0.0304` n `23`; metal avg `-0.0618` n `20`; unknown avg `1.3734` n `765`
- 24h: commodity avg `0.3604` n `12`; crypto_alt avg `-1.3184` n `228`; crypto_major avg `-1.2618` n `8`; equity avg `-2.6893` n `86`; fx avg `0.0717` n `6`; index avg `-0.2113` n `23`; metal avg `0.1605` n `20`; unknown avg `1.2176` n `716`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
