# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T04:22:16.328405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.2934` n `228`; crypto_major avg `-0.1728` n `8`; equity avg `-0.0065` n `67`; fx avg `0.0` n `6`; index avg `-0.0044` n `23`; metal avg `0.0018` n `18`; unknown avg `0.6797` n `386`
- 1h: commodity avg `0.178` n `12`; crypto_alt avg `-0.495` n `228`; crypto_major avg `-0.1058` n `8`; equity avg `-0.0148` n `67`; fx avg `-0.0012` n `6`; index avg `0.0019` n `23`; metal avg `-0.0276` n `18`; unknown avg `-0.1832` n `386`
- 4h: commodity avg `0.1343` n `12`; crypto_alt avg `0.5964` n `228`; crypto_major avg `0.4035` n `8`; equity avg `0.0973` n `67`; fx avg `-0.0045` n `6`; index avg `0.0702` n `23`; metal avg `0.011` n `18`; unknown avg `-0.9039` n `386`
- 24h: commodity avg `0.3337` n `12`; crypto_alt avg `-4.0565` n `228`; crypto_major avg `-2.6943` n `8`; equity avg `-1.9352` n `67`; fx avg `0.0646` n `6`; index avg `-0.0699` n `23`; metal avg `-0.949` n `18`; unknown avg `-2.0283` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
