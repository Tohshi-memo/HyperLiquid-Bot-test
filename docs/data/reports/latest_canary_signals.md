# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T08:07:32.055125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0329` n `230`; crypto_major avg `-0.0033` n `8`; equity avg `-0.0036` n `114`; fx avg `-0.0007` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.0026` n `791`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `0.301` n `230`; crypto_major avg `0.1004` n `8`; equity avg `-0.0377` n `114`; fx avg `0.0125` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.0045` n `791`
- 4h: commodity avg `-0.0316` n `12`; crypto_alt avg `0.2813` n `230`; crypto_major avg `0.0235` n `8`; equity avg `0.0751` n `114`; fx avg `0.0106` n `6`; index avg `0.016` n `25`; metal avg `0.0115` n `20`; unknown avg `-0.0122` n `759`
- 24h: commodity avg `0.1257` n `12`; crypto_alt avg `0.0876` n `230`; crypto_major avg `0.1109` n `8`; equity avg `0.3765` n `114`; fx avg `-0.0093` n `6`; index avg `0.058` n `25`; metal avg `0.0188` n `20`; unknown avg `-0.0898` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2101`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
