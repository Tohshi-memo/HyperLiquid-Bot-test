# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T18:52:24.283640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.1051` n `230`; crypto_major avg `-0.0866` n `8`; equity avg `0.0792` n `114`; fx avg `0.0055` n `6`; index avg `0.0155` n `25`; metal avg `-0.0073` n `20`; unknown avg `8.812` n `791`
- 1h: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.2247` n `230`; crypto_major avg `-0.2229` n `8`; equity avg `0.0011` n `114`; fx avg `0.0156` n `6`; index avg `0.025` n `25`; metal avg `-0.0004` n `20`; unknown avg `8.8663` n `791`
- 4h: commodity avg `0.0213` n `12`; crypto_alt avg `0.5485` n `230`; crypto_major avg `0.106` n `8`; equity avg `-0.4983` n `114`; fx avg `0.0513` n `6`; index avg `-0.0732` n `25`; metal avg `-0.0424` n `20`; unknown avg `18.9434` n `791`
- 24h: commodity avg `0.2521` n `12`; crypto_alt avg `0.3266` n `230`; crypto_major avg `-0.9561` n `8`; equity avg `-0.6895` n `114`; fx avg `0.0821` n `6`; index avg `-0.1128` n `25`; metal avg `0.1564` n `20`; unknown avg `0.0519` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
