# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T04:52:37.540350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0386` n `13`; crypto_alt avg `-0.1169` n `239`; crypto_major avg `0.0883` n `8`; equity avg `-0.1668` n `164`; fx avg `-0.0058` n `6`; index avg `-0.023` n `27`; metal avg `-0.0124` n `20`; unknown avg `3.1369` n `1266`
- 1h: commodity avg `0.0309` n `13`; crypto_alt avg `0.2561` n `239`; crypto_major avg `0.6833` n `8`; equity avg `-0.0333` n `164`; fx avg `0.0203` n `6`; index avg `-0.0013` n `27`; metal avg `0.0948` n `20`; unknown avg `3.4654` n `1246`
- 4h: commodity avg `0.0698` n `13`; crypto_alt avg `0.4933` n `239`; crypto_major avg `0.684` n `8`; equity avg `-0.4081` n `164`; fx avg `-0.0093` n `6`; index avg `-0.0471` n `27`; metal avg `-0.2744` n `20`; unknown avg `5.0658` n `1239`
- 24h: commodity avg `0.1425` n `13`; crypto_alt avg `0.6617` n `239`; crypto_major avg `-0.5225` n `8`; equity avg `-0.2551` n `164`; fx avg `-0.0951` n `6`; index avg `0.0653` n `27`; metal avg `-0.5343` n `20`; unknown avg `243.8259` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
