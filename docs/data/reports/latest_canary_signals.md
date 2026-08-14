# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T23:07:28.782405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.0534` n `230`; crypto_major avg `0.0659` n `8`; equity avg `-0.0022` n `114`; fx avg `0.006` n `6`; index avg `-0.0013` n `25`; metal avg `0.0105` n `20`; unknown avg `0.0072` n `791`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.0895` n `230`; crypto_major avg `0.0284` n `8`; equity avg `-0.0161` n `114`; fx avg `0.0005` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0015` n `20`; unknown avg `2.9735` n `791`
- 4h: commodity avg `0.0248` n `12`; crypto_alt avg `0.379` n `230`; crypto_major avg `0.3036` n `8`; equity avg `0.3465` n `114`; fx avg `0.0191` n `6`; index avg `0.0327` n `25`; metal avg `0.0549` n `20`; unknown avg `0.1094` n `791`
- 24h: commodity avg `0.2322` n `12`; crypto_alt avg `0.2806` n `230`; crypto_major avg `-0.8541` n `8`; equity avg `-0.5512` n `114`; fx avg `0.0858` n `6`; index avg `-0.0882` n `25`; metal avg `0.2506` n `20`; unknown avg `-0.0176` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
