# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T10:22:25.895481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `-0.0185` n `230`; crypto_major avg `-0.0163` n `8`; equity avg `-0.4597` n `102`; fx avg `-0.0132` n `6`; index avg `-0.051` n `25`; metal avg `-0.0205` n `20`; unknown avg `-0.0086` n `784`
- 1h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.1335` n `230`; crypto_major avg `0.2127` n `8`; equity avg `-0.8501` n `102`; fx avg `-0.0267` n `6`; index avg `-0.0936` n `25`; metal avg `-0.0742` n `20`; unknown avg `0.0611` n `784`
- 4h: commodity avg `0.035` n `12`; crypto_alt avg `0.0033` n `230`; crypto_major avg `0.0332` n `8`; equity avg `-1.4216` n `102`; fx avg `0.0134` n `6`; index avg `-0.1731` n `25`; metal avg `-0.2322` n `20`; unknown avg `-0.0161` n `784`
- 24h: commodity avg `-0.2632` n `12`; crypto_alt avg `-0.7251` n `230`; crypto_major avg `-0.0997` n `8`; equity avg `-0.805` n `102`; fx avg `-0.1992` n `6`; index avg `-0.1708` n `25`; metal avg `-0.1747` n `20`; unknown avg `1.0481` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
