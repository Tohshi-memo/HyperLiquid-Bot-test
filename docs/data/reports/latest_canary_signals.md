# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T06:52:25.931434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.1121` n `230`; crypto_major avg `0.0398` n `8`; equity avg `0.0019` n `114`; fx avg `-0.0053` n `6`; index avg `0.0023` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0184` n `791`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `0.0112` n `230`; crypto_major avg `0.0126` n `8`; equity avg `0.0469` n `114`; fx avg `-0.0012` n `6`; index avg `0.0101` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0299` n `759`
- 4h: commodity avg `-0.0004` n `12`; crypto_alt avg `0.1274` n `230`; crypto_major avg `-0.0909` n `8`; equity avg `0.1984` n `114`; fx avg `0.0004` n `6`; index avg `0.0182` n `25`; metal avg `0.0255` n `20`; unknown avg `-0.0008` n `759`
- 24h: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.295` n `230`; crypto_major avg `-0.1531` n `8`; equity avg `0.4061` n `114`; fx avg `-0.0158` n `6`; index avg `0.0543` n `25`; metal avg `0.0301` n `20`; unknown avg `0.0478` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
