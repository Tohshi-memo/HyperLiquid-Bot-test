# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T20:26:05.124376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `0.0096` n `230`; crypto_major avg `0.0066` n `8`; equity avg `0.0433` n `113`; fx avg `0.0001` n `6`; index avg `0.0034` n `25`; metal avg `0.0305` n `20`; unknown avg `-0.0162` n `787`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `0.0162` n `8`; equity avg `-0.1967` n `113`; fx avg `0.0009` n `6`; index avg `-0.0249` n `25`; metal avg `0.0249` n `20`; unknown avg `-0.0001` n `787`
- 4h: commodity avg `-0.2739` n `12`; crypto_alt avg `-0.1401` n `230`; crypto_major avg `0.0937` n `8`; equity avg `0.1004` n `113`; fx avg `0.0078` n `6`; index avg `0.0237` n `25`; metal avg `-0.0407` n `20`; unknown avg `0.0408` n `787`
- 24h: commodity avg `-0.4959` n `12`; crypto_alt avg `-0.2837` n `230`; crypto_major avg `0.3905` n `8`; equity avg `1.5837` n `113`; fx avg `0.011` n `6`; index avg `0.3075` n `25`; metal avg `-0.4973` n `20`; unknown avg `0.0606` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
