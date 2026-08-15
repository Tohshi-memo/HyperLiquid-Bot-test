# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T02:07:27.177232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.0907` n `230`; crypto_major avg `0.0639` n `8`; equity avg `0.0033` n `114`; fx avg `-0.0064` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.1791` n `791`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.0336` n `230`; crypto_major avg `0.1537` n `8`; equity avg `0.0363` n `114`; fx avg `-0.0084` n `6`; index avg `0.0037` n `25`; metal avg `-0.0261` n `20`; unknown avg `0.1491` n `791`
- 4h: commodity avg `-0.0123` n `12`; crypto_alt avg `0.255` n `230`; crypto_major avg `0.3382` n `8`; equity avg `-0.0077` n `114`; fx avg `-0.0322` n `6`; index avg `-0.0058` n `25`; metal avg `0.029` n `20`; unknown avg `0.3088` n `791`
- 24h: commodity avg `0.2293` n `12`; crypto_alt avg `-0.1443` n `230`; crypto_major avg `-0.7055` n `8`; equity avg `-0.1418` n `114`; fx avg `0.0977` n `6`; index avg `-0.0454` n `25`; metal avg `0.4914` n `20`; unknown avg `-0.188` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
