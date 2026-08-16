# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T20:52:26.821845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.1765` n `230`; crypto_major avg `-0.136` n `8`; equity avg `-0.0024` n `114`; fx avg `-0.0001` n `6`; index avg `-0.0105` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.3445` n `791`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.2108` n `230`; crypto_major avg `-0.1802` n `8`; equity avg `0.0019` n `114`; fx avg `0.0141` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0336` n `20`; unknown avg `0.4157` n `791`
- 4h: commodity avg `0.0631` n `12`; crypto_alt avg `-0.3386` n `230`; crypto_major avg `-0.3391` n `8`; equity avg `0.0128` n `114`; fx avg `0.0031` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0256` n `20`; unknown avg `0.131` n `791`
- 24h: commodity avg `0.0655` n `12`; crypto_alt avg `-0.4038` n `230`; crypto_major avg `-0.1874` n `8`; equity avg `0.2702` n `114`; fx avg `0.0004` n `6`; index avg `0.046` n `25`; metal avg `0.0188` n `20`; unknown avg `0.1385` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
