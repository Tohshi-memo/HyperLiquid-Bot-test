# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T08:22:31.463326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `-0.0243` n `230`; crypto_major avg `0.0115` n `8`; equity avg `-0.0004` n `114`; fx avg `0.0039` n `6`; index avg `0.0038` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.1259` n `791`
- 1h: commodity avg `0.0788` n `12`; crypto_alt avg `-0.0599` n `230`; crypto_major avg `-0.0086` n `8`; equity avg `-0.0188` n `114`; fx avg `0.0142` n `6`; index avg `-0.0146` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0454` n `791`
- 4h: commodity avg `-0.1677` n `12`; crypto_alt avg `0.0574` n `230`; crypto_major avg `-0.2044` n `8`; equity avg `-0.0608` n `114`; fx avg `0.0032` n `6`; index avg `-0.0226` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0791` n `759`
- 24h: commodity avg `-0.289` n `12`; crypto_alt avg `0.9389` n `230`; crypto_major avg `0.0967` n `8`; equity avg `-0.2975` n `114`; fx avg `0.1536` n `6`; index avg `-0.0911` n `25`; metal avg `0.2765` n `20`; unknown avg `-0.1191` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
