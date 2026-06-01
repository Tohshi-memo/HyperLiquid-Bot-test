# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T22:07:23.884907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.22` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1496` n `12`; crypto_alt avg `-0.4256` n `228`; crypto_major avg `-0.3775` n `8`; equity avg `-0.1524` n `69`; fx avg `-0.0039` n `6`; index avg `-0.0263` n `23`; metal avg `-0.0846` n `18`; unknown avg `-0.218` n `422`
- 1h: commodity avg `0.0876` n `12`; crypto_alt avg `-0.5451` n `228`; crypto_major avg `-0.4328` n `8`; equity avg `-0.1044` n `69`; fx avg `-0.0199` n `6`; index avg `-0.1246` n `23`; metal avg `-0.0124` n `18`; unknown avg `-0.3797` n `422`
- 4h: commodity avg `0.3571` n `12`; crypto_alt avg `-0.764` n `228`; crypto_major avg `-0.2942` n `8`; equity avg `-0.9543` n `69`; fx avg `-0.0203` n `6`; index avg `-0.4941` n `23`; metal avg `-0.3181` n `18`; unknown avg `-0.5718` n `422`
- 24h: commodity avg `-0.1426` n `12`; crypto_alt avg `-0.2334` n `228`; crypto_major avg `-1.4908` n `8`; equity avg `-0.2501` n `69`; fx avg `0.046` n `6`; index avg `-0.0225` n `23`; metal avg `0.183` n `18`; unknown avg `2.1647` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
