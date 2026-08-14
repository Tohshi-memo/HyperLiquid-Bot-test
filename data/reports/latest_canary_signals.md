# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T10:52:27.938441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0635` n `12`; crypto_alt avg `-0.029` n `230`; crypto_major avg `-0.0105` n `8`; equity avg `0.0363` n `113`; fx avg `-0.0006` n `6`; index avg `0.0005` n `25`; metal avg `0.0182` n `20`; unknown avg `-0.019` n `787`
- 1h: commodity avg `-0.1619` n `12`; crypto_alt avg `0.1174` n `230`; crypto_major avg `-0.0213` n `8`; equity avg `0.0957` n `113`; fx avg `0.0363` n `6`; index avg `0.0121` n `25`; metal avg `-0.0396` n `20`; unknown avg `0.1732` n `787`
- 4h: commodity avg `-0.1937` n `12`; crypto_alt avg `-0.1881` n `230`; crypto_major avg `-0.1469` n `8`; equity avg `0.4447` n `113`; fx avg `-0.0278` n `6`; index avg `0.065` n `25`; metal avg `0.1` n `20`; unknown avg `-0.01` n `787`
- 24h: commodity avg `-0.1309` n `12`; crypto_alt avg `-0.7735` n `230`; crypto_major avg `-0.7161` n `8`; equity avg `1.7925` n `113`; fx avg `-0.0522` n `6`; index avg `0.3433` n `25`; metal avg `-0.2501` n `20`; unknown avg `0.9494` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
