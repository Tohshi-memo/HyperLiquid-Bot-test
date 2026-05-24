# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T08:37:18.457009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1292` n `12`; crypto_alt avg `0.1493` n `228`; crypto_major avg `0.2889` n `8`; equity avg `-0.0588` n `67`; fx avg `0.004` n `6`; index avg `0.0231` n `23`; metal avg `-0.018` n `18`; unknown avg `0.0914` n `396`
- 1h: commodity avg `0.0564` n `12`; crypto_alt avg `0.1338` n `228`; crypto_major avg `0.3916` n `8`; equity avg `-0.0207` n `67`; fx avg `0.0048` n `6`; index avg `-0.0161` n `23`; metal avg `0.0811` n `18`; unknown avg `0.9238` n `396`
- 4h: commodity avg `0.259` n `12`; crypto_alt avg `0.057` n `228`; crypto_major avg `0.7725` n `8`; equity avg `0.0439` n `67`; fx avg `0.0052` n `6`; index avg `0.0421` n `23`; metal avg `0.1094` n `18`; unknown avg `1.1317` n `386`
- 24h: commodity avg `-2.6743` n `12`; crypto_alt avg `4.5318` n `228`; crypto_major avg `4.6479` n `8`; equity avg `2.6909` n `67`; fx avg `0.1024` n `6`; index avg `1.3746` n `23`; metal avg `1.2867` n `18`; unknown avg `3.1934` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
