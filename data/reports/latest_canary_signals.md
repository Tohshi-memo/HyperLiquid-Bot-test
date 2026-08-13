# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T02:42:05.797519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.1212` n `230`; crypto_major avg `-0.0181` n `8`; equity avg `-0.0841` n `113`; fx avg `0.0048` n `6`; index avg `-0.0195` n `25`; metal avg `-0.0888` n `20`; unknown avg `0.8595` n `786`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.1849` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `0.143` n `113`; fx avg `0.0199` n `6`; index avg `0.0141` n `25`; metal avg `-0.2035` n `20`; unknown avg `0.3101` n `786`
- 4h: commodity avg `-0.1044` n `12`; crypto_alt avg `0.2953` n `230`; crypto_major avg `0.2049` n `8`; equity avg `0.5666` n `113`; fx avg `-0.0289` n `6`; index avg `0.0575` n `25`; metal avg `-0.0259` n `20`; unknown avg `-0.1615` n `786`
- 24h: commodity avg `-0.263` n `12`; crypto_alt avg `-1.6034` n `230`; crypto_major avg `-0.5288` n `8`; equity avg `2.552` n `113`; fx avg `-0.0538` n `6`; index avg `0.2945` n `25`; metal avg `-0.1393` n `20`; unknown avg `-0.0131` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.238`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2017`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
