# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T08:22:32.617507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.1368` n `230`; crypto_major avg `-0.0538` n `8`; equity avg `0.1554` n `113`; fx avg `-0.0052` n `6`; index avg `0.0281` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0004` n `786`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.1681` n `230`; crypto_major avg `0.0173` n `8`; equity avg `0.3536` n `113`; fx avg `-0.023` n `6`; index avg `0.0539` n `25`; metal avg `0.0677` n `20`; unknown avg `0.0105` n `786`
- 4h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.5732` n `230`; crypto_major avg `-0.0403` n `8`; equity avg `0.4047` n `113`; fx avg `0.0084` n `6`; index avg `0.054` n `25`; metal avg `0.1309` n `20`; unknown avg `-0.0606` n `770`
- 24h: commodity avg `-0.1285` n `12`; crypto_alt avg `-1.1368` n `230`; crypto_major avg `0.8204` n `8`; equity avg `2.588` n `113`; fx avg `0.0022` n `6`; index avg `0.2695` n `25`; metal avg `0.2689` n `20`; unknown avg `-0.0906` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2308`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2279`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
