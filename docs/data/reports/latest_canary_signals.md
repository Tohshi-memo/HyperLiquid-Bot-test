# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T00:52:15.582722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `-0.0252` n `228`; crypto_major avg `0.0043` n `8`; equity avg `0.0726` n `67`; fx avg `0.0158` n `6`; index avg `0.0367` n `23`; metal avg `0.0215` n `18`; unknown avg `-0.0975` n `396`
- 1h: commodity avg `0.3032` n `12`; crypto_alt avg `0.0286` n `228`; crypto_major avg `0.2705` n `8`; equity avg `0.1034` n `67`; fx avg `-0.0115` n `6`; index avg `0.0707` n `23`; metal avg `0.083` n `18`; unknown avg `-0.2394` n `396`
- 4h: commodity avg `-0.5405` n `12`; crypto_alt avg `-0.6828` n `228`; crypto_major avg `-0.2591` n `8`; equity avg `0.4685` n `67`; fx avg `0.0357` n `6`; index avg `0.2158` n `23`; metal avg `0.2493` n `18`; unknown avg `0.1338` n `396`
- 24h: commodity avg `-2.8504` n `12`; crypto_alt avg `2.8073` n `228`; crypto_major avg `2.4763` n `8`; equity avg `2.2075` n `67`; fx avg `0.0478` n `6`; index avg `1.0943` n `23`; metal avg `1.0404` n `18`; unknown avg `1.2737` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
