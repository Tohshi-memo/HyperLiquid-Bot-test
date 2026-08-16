# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T12:37:31.564642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0233` n `230`; crypto_major avg `0.0003` n `8`; equity avg `-0.0656` n `114`; fx avg `0.0016` n `6`; index avg `-0.0042` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0005` n `791`
- 1h: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0472` n `230`; crypto_major avg `-0.0016` n `8`; equity avg `-0.0514` n `114`; fx avg `0.0023` n `6`; index avg `0.0008` n `25`; metal avg `0.0016` n `20`; unknown avg `0.0033` n `791`
- 4h: commodity avg `-0.0077` n `12`; crypto_alt avg `0.0586` n `230`; crypto_major avg `-0.1006` n `8`; equity avg `-0.1026` n `114`; fx avg `-0.0072` n `6`; index avg `-0.0061` n `25`; metal avg `0.0032` n `20`; unknown avg `0.1042` n `791`
- 24h: commodity avg `0.0339` n `12`; crypto_alt avg `0.1609` n `230`; crypto_major avg `0.1514` n `8`; equity avg `0.269` n `114`; fx avg `-0.0104` n `6`; index avg `0.0312` n `25`; metal avg `0.0356` n `20`; unknown avg `0.1203` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
