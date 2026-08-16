# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T10:35:59.270112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.0098` n `230`; crypto_major avg `0.0033` n `8`; equity avg `0.004` n `114`; fx avg `0.0` n `6`; index avg `-0.002` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0297` n `791`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.046` n `230`; crypto_major avg `-0.1307` n `8`; equity avg `-0.0137` n `114`; fx avg `-0.0047` n `6`; index avg `-0.0135` n `25`; metal avg `0.0027` n `20`; unknown avg `0.2364` n `791`
- 4h: commodity avg `0.0058` n `12`; crypto_alt avg `0.4493` n `230`; crypto_major avg `0.0762` n `8`; equity avg `-0.0179` n `114`; fx avg `-0.0034` n `6`; index avg `-0.0042` n `25`; metal avg `0.0007` n `20`; unknown avg `0.1556` n `791`
- 24h: commodity avg `0.1239` n `12`; crypto_alt avg `0.0134` n `230`; crypto_major avg `0.1163` n `8`; equity avg `0.3797` n `114`; fx avg `-0.0041` n `6`; index avg `0.0496` n `25`; metal avg `0.0329` n `20`; unknown avg `0.2447` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
