# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T22:37:22.916436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.0719` n `228`; crypto_major avg `-0.0979` n `8`; equity avg `-0.0046` n `74`; fx avg `-0.0065` n `6`; index avg `-0.0342` n `23`; metal avg `-0.025` n `18`; unknown avg `-0.2697` n `515`
- 1h: commodity avg `-0.0293` n `12`; crypto_alt avg `-0.2587` n `228`; crypto_major avg `-0.48` n `8`; equity avg `-0.203` n `74`; fx avg `0.0154` n `6`; index avg `-0.1776` n `23`; metal avg `-0.0141` n `18`; unknown avg `-0.1556` n `515`
- 4h: commodity avg `0.1036` n `12`; crypto_alt avg `0.097` n `228`; crypto_major avg `-0.2774` n `8`; equity avg `0.1661` n `74`; fx avg `-0.1547` n `6`; index avg `0.0287` n `23`; metal avg `-0.0135` n `18`; unknown avg `-0.2458` n `515`
- 24h: commodity avg `0.52` n `12`; crypto_alt avg `-2.1502` n `228`; crypto_major avg `-2.3722` n `8`; equity avg `-1.0558` n `74`; fx avg `0.0175` n `6`; index avg `-0.1346` n `23`; metal avg `-0.5631` n `18`; unknown avg `0.3907` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
