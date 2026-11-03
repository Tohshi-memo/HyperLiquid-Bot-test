# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T17:22:55.845908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.105` n `13`; crypto_alt avg `0.0138` n `239`; crypto_major avg `-0.0292` n `8`; equity avg `-0.0549` n `158`; fx avg `-0.0029` n `6`; index avg `-0.0125` n `27`; metal avg `-0.0191` n `20`; unknown avg `0.1252` n `1263`
- 1h: commodity avg `0.0943` n `13`; crypto_alt avg `0.3661` n `239`; crypto_major avg `0.3707` n `8`; equity avg `0.1471` n `158`; fx avg `0.0093` n `6`; index avg `0.0087` n `27`; metal avg `-0.0481` n `20`; unknown avg `-0.2286` n `1257`
- 4h: commodity avg `-0.1479` n `13`; crypto_alt avg `0.4846` n `239`; crypto_major avg `0.6939` n `8`; equity avg `0.9923` n `158`; fx avg `0.0482` n `6`; index avg `0.0937` n `27`; metal avg `-0.0499` n `20`; unknown avg `191.2187` n `1251`
- 24h: commodity avg `0.0308` n `13`; crypto_alt avg `0.5578` n `239`; crypto_major avg `1.1971` n `8`; equity avg `-0.3717` n `158`; fx avg `0.0446` n `6`; index avg `-0.0719` n `27`; metal avg `-0.6333` n `20`; unknown avg `0.2455` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
