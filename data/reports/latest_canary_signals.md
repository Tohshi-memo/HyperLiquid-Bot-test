# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T09:22:28.721079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1335` n `13`; crypto_alt avg `0.2042` n `239`; crypto_major avg `0.2198` n `8`; equity avg `0.3039` n `166`; fx avg `-0.0126` n `6`; index avg `0.0237` n `27`; metal avg `0.0687` n `20`; unknown avg `-0.1265` n `1264`
- 1h: commodity avg `-0.0713` n `13`; crypto_alt avg `0.4305` n `239`; crypto_major avg `0.7401` n `8`; equity avg `0.9082` n `166`; fx avg `-0.014` n `6`; index avg `0.0801` n `27`; metal avg `0.1897` n `20`; unknown avg `288.9055` n `1140`
- 4h: commodity avg `-0.4378` n `13`; crypto_alt avg `0.628` n `239`; crypto_major avg `0.5596` n `8`; equity avg `1.3727` n `166`; fx avg `-0.0184` n `6`; index avg `0.0778` n `27`; metal avg `0.1343` n `20`; unknown avg `288.663` n `1090`
- 24h: commodity avg `-0.7703` n `13`; crypto_alt avg `1.6964` n `239`; crypto_major avg `2.2489` n `8`; equity avg `2.9006` n `166`; fx avg `0.2063` n `6`; index avg `0.1861` n `27`; metal avg `0.5212` n `20`; unknown avg `1.1854` n `955`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
