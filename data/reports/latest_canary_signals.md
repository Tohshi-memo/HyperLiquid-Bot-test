# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T16:07:26.350669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.019` n `234`; crypto_major avg `-0.1012` n `8`; equity avg `-0.0138` n `140`; fx avg `0.0012` n `6`; index avg `-0.0055` n `26`; metal avg `-0.011` n `20`; unknown avg `4.0557` n `925`
- 1h: commodity avg `-0.0884` n `12`; crypto_alt avg `-0.2771` n `234`; crypto_major avg `-0.2651` n `8`; equity avg `-0.0068` n `140`; fx avg `-0.0147` n `6`; index avg `0.0004` n `26`; metal avg `-0.019` n `20`; unknown avg `4.2394` n `925`
- 4h: commodity avg `-0.13` n `12`; crypto_alt avg `-0.2739` n `234`; crypto_major avg `0.0964` n `8`; equity avg `0.0251` n `140`; fx avg `-0.0121` n `6`; index avg `0.0048` n `26`; metal avg `0.0068` n `20`; unknown avg `4.7768` n `922`
- 24h: commodity avg `-0.2312` n `12`; crypto_alt avg `2.3611` n `234`; crypto_major avg `1.2897` n `8`; equity avg `0.654` n `140`; fx avg `0.0339` n `6`; index avg `0.1601` n `26`; metal avg `0.0556` n `20`; unknown avg `3.2753` n `806`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
