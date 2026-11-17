# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T00:52:23.024528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `13`; crypto_alt avg `-0.124` n `239`; crypto_major avg `0.0239` n `8`; equity avg `0.0108` n `162`; fx avg `0.0103` n `6`; index avg `0.0117` n `27`; metal avg `-0.0392` n `20`; unknown avg `0.9764` n `1266`
- 1h: commodity avg `-0.0338` n `13`; crypto_alt avg `-0.5008` n `239`; crypto_major avg `-0.4869` n `8`; equity avg `-0.116` n `162`; fx avg `0.0168` n `6`; index avg `-0.0388` n `27`; metal avg `-0.0862` n `20`; unknown avg `1.0651` n `1258`
- 4h: commodity avg `-0.135` n `13`; crypto_alt avg `-0.6945` n `239`; crypto_major avg `-0.4082` n `8`; equity avg `-0.4754` n `162`; fx avg `0.015` n `6`; index avg `-0.0273` n `27`; metal avg `-0.0041` n `20`; unknown avg `2.6839` n `1190`
- 24h: commodity avg `-0.9903` n `13`; crypto_alt avg `-0.6557` n `239`; crypto_major avg `-0.2509` n `8`; equity avg `-4.4563` n `162`; fx avg `-0.0751` n `6`; index avg `-0.4755` n `27`; metal avg `-0.6695` n `20`; unknown avg `510.1335` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
