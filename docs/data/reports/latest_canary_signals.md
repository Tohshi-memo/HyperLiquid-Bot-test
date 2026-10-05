# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T18:52:35.760166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0384` n `13`; crypto_alt avg `-0.0116` n `235`; crypto_major avg `-0.0298` n `8`; equity avg `-0.0588` n `144`; fx avg `-0.0118` n `6`; index avg `-0.0054` n `26`; metal avg `0.0249` n `20`; unknown avg `0.4144` n `1079`
- 1h: commodity avg `-0.0919` n `13`; crypto_alt avg `0.2225` n `235`; crypto_major avg `0.0375` n `8`; equity avg `-0.1398` n `144`; fx avg `0.0009` n `6`; index avg `0.006` n `26`; metal avg `0.0603` n `20`; unknown avg `2.1291` n `1077`
- 4h: commodity avg `-0.2703` n `13`; crypto_alt avg `0.3697` n `235`; crypto_major avg `0.0709` n `8`; equity avg `0.091` n `144`; fx avg `0.0113` n `6`; index avg `0.0668` n `26`; metal avg `0.0184` n `20`; unknown avg `3.029` n `1041`
- 24h: commodity avg `-0.4484` n `13`; crypto_alt avg `0.0522` n `235`; crypto_major avg `0.1737` n `8`; equity avg `0.2461` n `144`; fx avg `-0.0929` n `6`; index avg `0.124` n `26`; metal avg `0.208` n `20`; unknown avg `2.0323` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.201`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
