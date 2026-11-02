# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T05:07:34.798260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0605` n `13`; crypto_alt avg `-0.0243` n `238`; crypto_major avg `-0.0089` n `8`; equity avg `-0.1515` n `156`; fx avg `-0.0036` n `6`; index avg `-0.0149` n `27`; metal avg `0.038` n `20`; unknown avg `-0.6494` n `1255`
- 1h: commodity avg `-0.0058` n `13`; crypto_alt avg `-0.2952` n `238`; crypto_major avg `-0.3768` n `8`; equity avg `-0.2748` n `156`; fx avg `-0.006` n `6`; index avg `-0.0087` n `27`; metal avg `-0.011` n `20`; unknown avg `-0.5667` n `1255`
- 4h: commodity avg `-0.3681` n `13`; crypto_alt avg `-0.0168` n `238`; crypto_major avg `0.2579` n `8`; equity avg `0.4991` n `156`; fx avg `0.086` n `6`; index avg `0.105` n `27`; metal avg `-0.1172` n `20`; unknown avg `1.0228` n `1193`
- 24h: commodity avg `-0.43` n `13`; crypto_alt avg `-0.7112` n `238`; crypto_major avg `0.355` n `8`; equity avg `1.2371` n `156`; fx avg `0.1998` n `6`; index avg `0.345` n `27`; metal avg `0.0805` n `20`; unknown avg `3.367` n `1074`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
