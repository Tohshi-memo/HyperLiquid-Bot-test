# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T07:37:21.912882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.0731` n `228`; crypto_major avg `-0.1416` n `8`; equity avg `0.012` n `69`; fx avg `0.0` n `6`; index avg `-0.0053` n `23`; metal avg `-0.0003` n `18`; unknown avg `-0.0047` n `421`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.4258` n `228`; crypto_major avg `-0.0817` n `8`; equity avg `0.0046` n `69`; fx avg `0.0005` n `6`; index avg `0.0348` n `23`; metal avg `0.0062` n `18`; unknown avg `-0.1308` n `421`
- 4h: commodity avg `-0.105` n `12`; crypto_alt avg `-0.2769` n `228`; crypto_major avg `0.1136` n `8`; equity avg `0.1933` n `69`; fx avg `0.0024` n `6`; index avg `0.167` n `23`; metal avg `-0.0009` n `18`; unknown avg `0.1463` n `401`
- 24h: commodity avg `-0.6481` n `12`; crypto_alt avg `1.5001` n `228`; crypto_major avg `1.9767` n `8`; equity avg `1.0118` n `69`; fx avg `0.0527` n `6`; index avg `0.1717` n `23`; metal avg `-0.0069` n `18`; unknown avg `0.3129` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
