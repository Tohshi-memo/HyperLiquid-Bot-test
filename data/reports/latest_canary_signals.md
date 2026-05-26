# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T10:37:19.717610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3358` n `12`; crypto_alt avg `0.5817` n `228`; crypto_major avg `0.6491` n `8`; equity avg `0.1525` n `67`; fx avg `-0.04` n `6`; index avg `0.1197` n `23`; metal avg `0.1256` n `18`; unknown avg `1.6477` n `417`
- 1h: commodity avg `-0.6052` n `12`; crypto_alt avg `1.2376` n `228`; crypto_major avg `1.3292` n `8`; equity avg `0.308` n `67`; fx avg `-0.048` n `6`; index avg `0.1924` n `23`; metal avg `0.2688` n `18`; unknown avg `2.3391` n `417`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `1.1129` n `228`; crypto_major avg `0.8276` n `8`; equity avg `0.4135` n `67`; fx avg `-0.0171` n `6`; index avg `0.2723` n `23`; metal avg `-0.0932` n `18`; unknown avg `1.2821` n `417`
- 24h: commodity avg `0.4147` n `12`; crypto_alt avg `0.1518` n `228`; crypto_major avg `-0.4364` n `8`; equity avg `-0.2935` n `67`; fx avg `-0.1226` n `6`; index avg `0.1648` n `23`; metal avg `-0.7579` n `18`; unknown avg `0.9154` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
