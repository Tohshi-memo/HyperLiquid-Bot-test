# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T02:37:28.749873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.0459` n `230`; crypto_major avg `0.0925` n `8`; equity avg `0.0107` n `114`; fx avg `-0.0011` n `6`; index avg `-0.0012` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0313` n `791`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `-0.0054` n `230`; crypto_major avg `0.1672` n `8`; equity avg `0.0464` n `114`; fx avg `0.003` n `6`; index avg `0.0021` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0189` n `791`
- 4h: commodity avg `0.0813` n `12`; crypto_alt avg `-0.5538` n `230`; crypto_major avg `-0.0316` n `8`; equity avg `0.0227` n `114`; fx avg `0.0032` n `6`; index avg `0.0156` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0424` n `791`
- 24h: commodity avg `0.0123` n `12`; crypto_alt avg `-0.077` n `230`; crypto_major avg `0.0683` n `8`; equity avg `0.1896` n `114`; fx avg `-0.0749` n `6`; index avg `0.0135` n `25`; metal avg `-0.0153` n `20`; unknown avg `0.0719` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2231`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
