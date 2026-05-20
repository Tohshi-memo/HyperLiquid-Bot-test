# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T10:22:21.272625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `-0.0062` n `228`; crypto_major avg `0.1181` n `8`; equity avg `0.0019` n `66`; fx avg `0.0145` n `6`; index avg `0.0176` n `23`; metal avg `-0.0126` n `18`; unknown avg `0.3915` n `384`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0208` n `228`; crypto_major avg `0.2029` n `8`; equity avg `0.234` n `66`; fx avg `0.011` n `6`; index avg `0.0531` n `23`; metal avg `0.1542` n `18`; unknown avg `1.0027` n `384`
- 4h: commodity avg `-0.3066` n `12`; crypto_alt avg `0.2129` n `228`; crypto_major avg `0.3846` n `8`; equity avg `0.5847` n `66`; fx avg `-0.0395` n `6`; index avg `0.2724` n `23`; metal avg `0.4749` n `18`; unknown avg `0.431` n `384`
- 24h: commodity avg `-0.0917` n `12`; crypto_alt avg `0.779` n `228`; crypto_major avg `0.7356` n `8`; equity avg `1.5628` n `66`; fx avg `-0.1544` n `6`; index avg `0.2433` n `23`; metal avg `-0.7079` n `18`; unknown avg `1.0476` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
