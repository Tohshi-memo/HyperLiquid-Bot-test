# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T19:07:29.987608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `-0.2225` n `228`; crypto_major avg `-0.2743` n `8`; equity avg `-0.0997` n `85`; fx avg `0.0042` n `6`; index avg `-0.0094` n `23`; metal avg `0.0076` n `20`; unknown avg `-0.1943` n `717`
- 1h: commodity avg `0.0065` n `12`; crypto_alt avg `-0.6635` n `228`; crypto_major avg `-0.532` n `8`; equity avg `-0.3645` n `85`; fx avg `-0.0083` n `6`; index avg `-0.0892` n `23`; metal avg `0.0805` n `20`; unknown avg `-0.3141` n `717`
- 4h: commodity avg `-0.0696` n `12`; crypto_alt avg `-1.1465` n `228`; crypto_major avg `-0.758` n `8`; equity avg `-0.4228` n `85`; fx avg `-0.0065` n `6`; index avg `-0.0852` n `23`; metal avg `-0.0978` n `20`; unknown avg `-0.3929` n `716`
- 24h: commodity avg `-0.9712` n `12`; crypto_alt avg `-1.072` n `228`; crypto_major avg `-0.4472` n `8`; equity avg `-0.7131` n `85`; fx avg `0.0375` n `6`; index avg `0.0624` n `23`; metal avg `0.3289` n `18`; unknown avg `0.6395` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
