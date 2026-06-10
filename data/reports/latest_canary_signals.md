# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T17:22:28.804707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.2867` n `228`; crypto_major avg `-0.3679` n `8`; equity avg `-0.3117` n `74`; fx avg `-0.0034` n `6`; index avg `-0.1149` n `23`; metal avg `-0.2737` n `18`; unknown avg `-0.0029` n `548`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-1.1212` n `228`; crypto_major avg `-1.2995` n `8`; equity avg `-0.7482` n `74`; fx avg `0.0214` n `6`; index avg `-0.4088` n `23`; metal avg `-0.4311` n `18`; unknown avg `4.7933` n `548`
- 4h: commodity avg `0.449` n `12`; crypto_alt avg `-0.0779` n `228`; crypto_major avg `0.0071` n `8`; equity avg `0.028` n `74`; fx avg `-0.0142` n `6`; index avg `-0.2586` n `23`; metal avg `-0.0456` n `18`; unknown avg `2.8614` n `547`
- 24h: commodity avg `1.8926` n `12`; crypto_alt avg `-0.6409` n `228`; crypto_major avg `-1.375` n `8`; equity avg `-0.1051` n `74`; fx avg `-0.0431` n `6`; index avg `0.0743` n `23`; metal avg `-1.5312` n `18`; unknown avg `-0.0238` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
