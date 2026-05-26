# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T22:44:19.821158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.0659` n `228`; crypto_major avg `-0.1086` n `8`; equity avg `-0.0047` n `67`; fx avg `0.0027` n `6`; index avg `0.0586` n `23`; metal avg `-0.0651` n `18`; unknown avg `-0.0191` n `418`
- 1h: commodity avg `-0.2214` n `12`; crypto_alt avg `-0.366` n `228`; crypto_major avg `-0.1561` n `8`; equity avg `-0.0099` n `67`; fx avg `0.0299` n `6`; index avg `-0.0339` n `23`; metal avg `0.0025` n `18`; unknown avg `0.061` n `418`
- 4h: commodity avg `-0.115` n `12`; crypto_alt avg `-0.3145` n `228`; crypto_major avg `-0.6135` n `8`; equity avg `0.0088` n `67`; fx avg `0.0289` n `6`; index avg `0.005` n `23`; metal avg `0.4521` n `18`; unknown avg `-0.2206` n `418`
- 24h: commodity avg `0.8669` n `12`; crypto_alt avg `-1.3703` n `228`; crypto_major avg `-1.4507` n `8`; equity avg `-0.1751` n `67`; fx avg `-0.1198` n `6`; index avg `0.5452` n `23`; metal avg `-0.8063` n `18`; unknown avg `0.2226` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
