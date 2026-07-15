# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T10:52:25.885077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `-0.048` n `230`; crypto_major avg `0.0328` n `8`; equity avg `0.0143` n `93`; fx avg `0.0023` n `6`; index avg `0.0029` n `25`; metal avg `-0.049` n `20`; unknown avg `0.0145` n `767`
- 1h: commodity avg `-0.0096` n `12`; crypto_alt avg `0.0607` n `230`; crypto_major avg `0.0141` n `8`; equity avg `-0.0995` n `93`; fx avg `-0.0198` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0809` n `20`; unknown avg `-0.0285` n `767`
- 4h: commodity avg `0.0699` n `12`; crypto_alt avg `-0.2197` n `230`; crypto_major avg `-0.2944` n `8`; equity avg `-0.2806` n `93`; fx avg `-0.0107` n `6`; index avg `-0.0874` n `25`; metal avg `-0.1104` n `20`; unknown avg `-0.144` n `765`
- 24h: commodity avg `-0.1816` n `12`; crypto_alt avg `1.6113` n `230`; crypto_major avg `2.8965` n `8`; equity avg `1.0608` n `92`; fx avg `0.006` n `6`; index avg `0.3736` n `25`; metal avg `0.2283` n `20`; unknown avg `0.2403` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
