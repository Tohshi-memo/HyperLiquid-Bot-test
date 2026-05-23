# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T14:52:19.611228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0614` n `12`; crypto_alt avg `0.1703` n `228`; crypto_major avg `0.2051` n `8`; equity avg `0.2029` n `67`; fx avg `0.0019` n `6`; index avg `0.0099` n `23`; metal avg `-0.0045` n `18`; unknown avg `0.3859` n `396`
- 1h: commodity avg `-0.7617` n `12`; crypto_alt avg `0.6047` n `228`; crypto_major avg `0.5635` n `8`; equity avg `0.466` n `67`; fx avg `0.004` n `6`; index avg `0.2655` n `23`; metal avg `0.0759` n `18`; unknown avg `0.838` n `396`
- 4h: commodity avg `-0.7012` n `12`; crypto_alt avg `1.4232` n `228`; crypto_major avg `1.0485` n `8`; equity avg `0.6332` n `67`; fx avg `-0.0042` n `6`; index avg `0.5853` n `23`; metal avg `0.1314` n `18`; unknown avg `0.8346` n `396`
- 24h: commodity avg `-0.4582` n `12`; crypto_alt avg `-3.5845` n `228`; crypto_major avg `-2.6407` n `8`; equity avg `-0.9632` n `67`; fx avg `0.0687` n `6`; index avg `0.0817` n `23`; metal avg `0.0784` n `18`; unknown avg `-2.5189` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
