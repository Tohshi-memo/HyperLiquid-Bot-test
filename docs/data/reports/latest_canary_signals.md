# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T21:14:54.250220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.1694` n `228`; crypto_major avg `0.1678` n `8`; equity avg `0.035` n `67`; fx avg `0.0106` n `6`; index avg `-0.0443` n `23`; metal avg `-0.0321` n `18`; unknown avg `0.0436` n `396`
- 1h: commodity avg `0.1951` n `12`; crypto_alt avg `-0.1231` n `228`; crypto_major avg `-0.0894` n `8`; equity avg `0.031` n `67`; fx avg `0.0148` n `6`; index avg `-0.094` n `23`; metal avg `-0.1236` n `18`; unknown avg `-0.2061` n `396`
- 4h: commodity avg `0.1983` n `12`; crypto_alt avg `-0.5031` n `228`; crypto_major avg `-0.4342` n `8`; equity avg `0.1151` n `67`; fx avg `0.055` n `6`; index avg `-0.0417` n `23`; metal avg `-0.2584` n `18`; unknown avg `-0.5389` n `396`
- 24h: commodity avg `1.1975` n `12`; crypto_alt avg `-2.5138` n `228`; crypto_major avg `-0.4621` n `8`; equity avg `0.6057` n `67`; fx avg `0.1114` n `6`; index avg `-0.0416` n `23`; metal avg `-0.4279` n `18`; unknown avg `0.0564` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
