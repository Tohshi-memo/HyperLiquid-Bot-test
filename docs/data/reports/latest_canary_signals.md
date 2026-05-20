# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T19:22:18.289755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.072` n `12`; crypto_alt avg `0.3985` n `228`; crypto_major avg `0.3521` n `8`; equity avg `0.0983` n `66`; fx avg `-0.0057` n `6`; index avg `0.0976` n `23`; metal avg `0.0009` n `18`; unknown avg `0.0642` n `384`
- 1h: commodity avg `0.2144` n `12`; crypto_alt avg `0.088` n `228`; crypto_major avg `-0.044` n `8`; equity avg `-0.0801` n `66`; fx avg `0.0205` n `6`; index avg `0.154` n `23`; metal avg `0.1411` n `18`; unknown avg `-0.1361` n `384`
- 4h: commodity avg `-0.0984` n `12`; crypto_alt avg `0.2732` n `228`; crypto_major avg `-0.0539` n `8`; equity avg `0.051` n `66`; fx avg `0.0426` n `6`; index avg `0.182` n `23`; metal avg `0.0194` n `18`; unknown avg `0.7223` n `384`
- 24h: commodity avg `-2.6112` n `12`; crypto_alt avg `2.7944` n `228`; crypto_major avg `1.8941` n `8`; equity avg `1.4895` n `66`; fx avg `-0.019` n `6`; index avg `0.9925` n `23`; metal avg `1.5932` n `18`; unknown avg `1.0546` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
