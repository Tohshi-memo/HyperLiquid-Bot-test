# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T07:22:16.487399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3071` n `12`; crypto_alt avg `-0.1725` n `228`; crypto_major avg `-0.1408` n `8`; equity avg `0.0466` n `67`; fx avg `0.0049` n `6`; index avg `-0.0074` n `23`; metal avg `-0.0591` n `18`; unknown avg `-0.0446` n `396`
- 1h: commodity avg `0.387` n `12`; crypto_alt avg `0.1462` n `228`; crypto_major avg `0.3137` n `8`; equity avg `0.224` n `67`; fx avg `-0.0063` n `6`; index avg `0.1076` n `23`; metal avg `-0.066` n `18`; unknown avg `-0.236` n `396`
- 4h: commodity avg `0.0847` n `12`; crypto_alt avg `-0.2087` n `228`; crypto_major avg `0.2546` n `8`; equity avg `0.153` n `67`; fx avg `0.0127` n `6`; index avg `0.0119` n `23`; metal avg `-0.0441` n `18`; unknown avg `-0.097` n `386`
- 24h: commodity avg `-2.6213` n `12`; crypto_alt avg `2.1359` n `228`; crypto_major avg `3.1405` n `8`; equity avg `2.456` n `67`; fx avg `0.033` n `6`; index avg `1.3317` n `23`; metal avg `1.121` n `18`; unknown avg `1.8316` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
