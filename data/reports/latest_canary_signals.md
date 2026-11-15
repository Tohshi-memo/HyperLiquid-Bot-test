# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T22:52:23.849046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `-0.0297` n `239`; crypto_major avg `0.0082` n `8`; equity avg `0.0685` n `162`; fx avg `0.006` n `6`; index avg `0.0119` n `27`; metal avg `0.0284` n `20`; unknown avg `0.1322` n `1235`
- 1h: commodity avg `-0.0194` n `13`; crypto_alt avg `0.333` n `239`; crypto_major avg `0.1282` n `8`; equity avg `0.1011` n `162`; fx avg `-0.0043` n `6`; index avg `0.0117` n `27`; metal avg `0.0357` n `20`; unknown avg `0.4002` n `1211`
- 4h: commodity avg `-0.0271` n `13`; crypto_alt avg `1.0929` n `239`; crypto_major avg `1.2593` n `8`; equity avg `0.7131` n `162`; fx avg `0.0288` n `6`; index avg `0.0669` n `27`; metal avg `0.0652` n `20`; unknown avg `1.7723` n `1185`
- 24h: commodity avg `-0.0681` n `13`; crypto_alt avg `3.6045` n `239`; crypto_major avg `4.7021` n `8`; equity avg `1.4929` n `162`; fx avg `0.0122` n `6`; index avg `0.1199` n `27`; metal avg `0.2797` n `20`; unknown avg `45.8781` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
