# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T10:22:28.412643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.0437` n `230`; crypto_major avg `-0.0554` n `8`; equity avg `0.0015` n `93`; fx avg `-0.0136` n `6`; index avg `0.0031` n `25`; metal avg `-0.0163` n `20`; unknown avg `0.0431` n `767`
- 1h: commodity avg `0.0258` n `12`; crypto_alt avg `-0.0843` n `230`; crypto_major avg `-0.2361` n `8`; equity avg `-0.1043` n `93`; fx avg `-0.009` n `6`; index avg `-0.0279` n `25`; metal avg `-0.086` n `20`; unknown avg `-0.0417` n `767`
- 4h: commodity avg `0.1457` n `12`; crypto_alt avg `-0.13` n `230`; crypto_major avg `-0.2792` n `8`; equity avg `-0.2093` n `93`; fx avg `0.0099` n `6`; index avg `-0.0611` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.1859` n `765`
- 24h: commodity avg `-0.0795` n `12`; crypto_alt avg `1.7425` n `230`; crypto_major avg `3.2337` n `8`; equity avg `1.1277` n `92`; fx avg `0.029` n `6`; index avg `0.3974` n `25`; metal avg `0.2844` n `20`; unknown avg `0.2774` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
