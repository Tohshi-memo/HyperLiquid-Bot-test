# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T04:04:27.003820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `-0.0489` n `230`; crypto_major avg `-0.0296` n `8`; equity avg `0.009` n `114`; fx avg `0.0045` n `6`; index avg `0.0017` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.0559` n `791`
- 1h: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0788` n `230`; crypto_major avg `-0.0782` n `8`; equity avg `0.0965` n `114`; fx avg `-0.0004` n `6`; index avg `0.0075` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0263` n `791`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `-0.1482` n `230`; crypto_major avg `0.1047` n `8`; equity avg `0.1432` n `114`; fx avg `0.005` n `6`; index avg `0.0098` n `25`; metal avg `0.0186` n `20`; unknown avg `-0.0105` n `791`
- 24h: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.012` n `230`; crypto_major avg `-0.0856` n `8`; equity avg `0.231` n `114`; fx avg `-0.0155` n `6`; index avg `0.0165` n `25`; metal avg `0.0182` n `20`; unknown avg `-0.0504` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2214`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
