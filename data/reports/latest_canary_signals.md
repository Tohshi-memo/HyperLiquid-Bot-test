# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T23:07:30.991256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `12`; crypto_alt avg `-0.1068` n `228`; crypto_major avg `-0.0346` n `8`; equity avg `0.0172` n `78`; fx avg `0.0013` n `6`; index avg `0.0014` n `23`; metal avg `-0.0006` n `18`; unknown avg `0.1123` n `701`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `0.4274` n `228`; crypto_major avg `0.4821` n `8`; equity avg `0.1034` n `78`; fx avg `-0.0007` n `6`; index avg `0.0404` n `23`; metal avg `0.0131` n `18`; unknown avg `-0.098` n `701`
- 4h: commodity avg `0.0193` n `12`; crypto_alt avg `0.7131` n `228`; crypto_major avg `1.0224` n `8`; equity avg `0.3277` n `78`; fx avg `0.0048` n `6`; index avg `0.0434` n `23`; metal avg `0.0118` n `18`; unknown avg `0.4573` n `701`
- 24h: commodity avg `0.2953` n `12`; crypto_alt avg `1.3823` n `228`; crypto_major avg `1.8681` n `8`; equity avg `0.5627` n `78`; fx avg `0.0907` n `6`; index avg `0.1043` n `23`; metal avg `-0.0451` n `18`; unknown avg `-0.4449` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
