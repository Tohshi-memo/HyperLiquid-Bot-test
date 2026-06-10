# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T18:52:31.004749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0312` n `12`; crypto_alt avg `0.0533` n `228`; crypto_major avg `-0.0374` n `8`; equity avg `-0.1707` n `74`; fx avg `0.0022` n `6`; index avg `-0.0886` n `23`; metal avg `-0.1421` n `18`; unknown avg `-0.0317` n `550`
- 1h: commodity avg `-0.5512` n `12`; crypto_alt avg `-0.1705` n `228`; crypto_major avg `-0.3743` n `8`; equity avg `-0.457` n `74`; fx avg `0.0173` n `6`; index avg `-0.2867` n `23`; metal avg `-0.1138` n `18`; unknown avg `0.2639` n `550`
- 4h: commodity avg `0.0295` n `12`; crypto_alt avg `-1.1199` n `228`; crypto_major avg `-1.4677` n `8`; equity avg `-1.4681` n `74`; fx avg `-0.0085` n `6`; index avg `-1.0521` n `23`; metal avg `-0.5952` n `18`; unknown avg `0.1903` n `548`
- 24h: commodity avg `1.2579` n `12`; crypto_alt avg `-1.2758` n `228`; crypto_major avg `-2.2042` n `8`; equity avg `-1.1566` n `74`; fx avg `-0.0365` n `6`; index avg `-0.7798` n `23`; metal avg `-1.8629` n `18`; unknown avg `-0.1263` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
