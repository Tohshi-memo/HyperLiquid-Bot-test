# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T01:52:37.503964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.2052` n `239`; crypto_major avg `0.2885` n `8`; equity avg `0.0228` n `162`; fx avg `-0.0114` n `6`; index avg `0.0162` n `27`; metal avg `0.0754` n `20`; unknown avg `0.2627` n `1266`
- 1h: commodity avg `-0.0608` n `13`; crypto_alt avg `0.3549` n `239`; crypto_major avg `0.4753` n `8`; equity avg `0.4033` n `162`; fx avg `0.02` n `6`; index avg `0.0514` n `27`; metal avg `0.1822` n `20`; unknown avg `0.4568` n `1264`
- 4h: commodity avg `-0.0236` n `13`; crypto_alt avg `-0.6495` n `239`; crypto_major avg `-0.5716` n `8`; equity avg `-0.0099` n `162`; fx avg `0.0454` n `6`; index avg `0.0306` n `27`; metal avg `0.1688` n `20`; unknown avg `6.5957` n `1220`
- 24h: commodity avg `-1.0139` n `13`; crypto_alt avg `0.4922` n `239`; crypto_major avg `0.9383` n `8`; equity avg `-2.6588` n `162`; fx avg `-0.0654` n `6`; index avg `-0.253` n `27`; metal avg `-0.0636` n `20`; unknown avg `513.6658` n `997`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
