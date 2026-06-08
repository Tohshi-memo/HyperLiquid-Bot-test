# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T10:52:20.243132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `12`; crypto_alt avg `-0.2265` n `228`; crypto_major avg `-0.1957` n `8`; equity avg `-0.001` n `74`; fx avg `0.0042` n `6`; index avg `-0.0092` n `23`; metal avg `-0.1114` n `18`; unknown avg `0.115` n `517`
- 1h: commodity avg `-0.1604` n `12`; crypto_alt avg `-0.0015` n `228`; crypto_major avg `-0.2331` n `8`; equity avg `0.0433` n `74`; fx avg `0.071` n `6`; index avg `0.0437` n `23`; metal avg `-0.0203` n `18`; unknown avg `-0.0401` n `517`
- 4h: commodity avg `-0.3173` n `12`; crypto_alt avg `0.6138` n `228`; crypto_major avg `-0.094` n `8`; equity avg `0.9574` n `74`; fx avg `-0.0137` n `6`; index avg `0.3849` n `23`; metal avg `-0.0346` n `18`; unknown avg `-0.2057` n `517`
- 24h: commodity avg `0.5406` n `12`; crypto_alt avg `0.9905` n `228`; crypto_major avg `1.6902` n `8`; equity avg `1.3107` n `74`; fx avg `-0.2535` n `6`; index avg `0.5618` n `23`; metal avg `-0.6586` n `18`; unknown avg `-2.3916` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
