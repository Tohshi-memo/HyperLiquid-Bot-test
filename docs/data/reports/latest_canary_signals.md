# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T14:07:27.754135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1091` n `12`; crypto_alt avg `-0.1451` n `230`; crypto_major avg `-0.0664` n `8`; equity avg `0.2174` n `114`; fx avg `0.0013` n `6`; index avg `0.0475` n `25`; metal avg `0.068` n `20`; unknown avg `-0.1591` n `786`
- 1h: commodity avg `0.0796` n `12`; crypto_alt avg `-0.0379` n `230`; crypto_major avg `-0.055` n `8`; equity avg `0.103` n `114`; fx avg `0.0447` n `6`; index avg `0.0186` n `25`; metal avg `0.1082` n `20`; unknown avg `-0.2933` n `786`
- 4h: commodity avg `0.0383` n `12`; crypto_alt avg `-0.0059` n `230`; crypto_major avg `-0.3919` n `8`; equity avg `0.2186` n `114`; fx avg `0.0525` n `6`; index avg `0.0255` n `25`; metal avg `0.2266` n `20`; unknown avg `3.2056` n `786`
- 24h: commodity avg `0.3077` n `12`; crypto_alt avg `-0.9105` n `230`; crypto_major avg `-1.2138` n `8`; equity avg `0.6104` n `114`; fx avg `0.0162` n `6`; index avg `0.1566` n `25`; metal avg `0.1569` n `20`; unknown avg `0.0226` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1983`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
