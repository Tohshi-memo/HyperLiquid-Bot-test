# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T00:37:21.031951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1219` n `12`; crypto_alt avg `0.2065` n `228`; crypto_major avg `0.3035` n `8`; equity avg `0.0605` n `67`; fx avg `-0.0223` n `6`; index avg `-0.0004` n `23`; metal avg `0.0326` n `18`; unknown avg `-0.1051` n `396`
- 1h: commodity avg `0.1703` n `12`; crypto_alt avg `0.0403` n `228`; crypto_major avg `0.2551` n `8`; equity avg `0.0294` n `67`; fx avg `-0.0275` n `6`; index avg `0.0726` n `23`; metal avg `0.106` n `18`; unknown avg `0.2033` n `396`
- 4h: commodity avg `-0.508` n `12`; crypto_alt avg `0.3358` n `228`; crypto_major avg `0.4293` n `8`; equity avg `0.6117` n `67`; fx avg `0.0391` n `6`; index avg `0.1677` n `23`; metal avg `0.4028` n `18`; unknown avg `-0.1166` n `396`
- 24h: commodity avg `-2.8294` n `12`; crypto_alt avg `3.0631` n `228`; crypto_major avg `2.6924` n `8`; equity avg `2.2089` n `67`; fx avg `0.0315` n `6`; index avg `1.053` n `23`; metal avg `1.0155` n `18`; unknown avg `1.1811` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
