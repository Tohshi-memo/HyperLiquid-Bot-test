# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T00:52:28.000874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0747` n `12`; crypto_alt avg `0.1969` n `228`; crypto_major avg `0.0918` n `8`; equity avg `-0.0289` n `74`; fx avg `0.0` n `6`; index avg `-0.0794` n `23`; metal avg `0.0193` n `18`; unknown avg `-0.1641` n `425`
- 1h: commodity avg `0.3743` n `12`; crypto_alt avg `1.0305` n `228`; crypto_major avg `1.0237` n `8`; equity avg `0.3655` n `74`; fx avg `-0.0001` n `6`; index avg `0.1639` n `23`; metal avg `0.0872` n `18`; unknown avg `0.8916` n `425`
- 4h: commodity avg `0.5741` n `12`; crypto_alt avg `0.0717` n `228`; crypto_major avg `0.066` n `8`; equity avg `0.0077` n `74`; fx avg `0.0007` n `6`; index avg `0.317` n `23`; metal avg `-0.0579` n `18`; unknown avg `0.4044` n `425`
- 24h: commodity avg `-1.0318` n `12`; crypto_alt avg `-5.812` n `228`; crypto_major avg `-5.028` n `8`; equity avg `-5.2267` n `74`; fx avg `-0.1267` n `6`; index avg `-3.4273` n `23`; metal avg `-4.1073` n `18`; unknown avg `-1.014` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
