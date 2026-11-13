# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T19:22:34.795471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `0.0506` n `239`; crypto_major avg `-0.0179` n `8`; equity avg `0.118` n `162`; fx avg `0.0018` n `6`; index avg `0.0195` n `27`; metal avg `-0.0196` n `20`; unknown avg `0.0074` n `1260`
- 1h: commodity avg `-0.0266` n `13`; crypto_alt avg `0.2712` n `239`; crypto_major avg `0.2167` n `8`; equity avg `0.6329` n `162`; fx avg `0.0058` n `6`; index avg `0.0907` n `27`; metal avg `-0.0632` n `20`; unknown avg `0.3965` n `1260`
- 4h: commodity avg `-0.2333` n `13`; crypto_alt avg `0.4107` n `239`; crypto_major avg `0.5031` n `8`; equity avg `1.5651` n `162`; fx avg `-0.0837` n `6`; index avg `0.1377` n `27`; metal avg `-0.1295` n `20`; unknown avg `-0.2816` n `1254`
- 24h: commodity avg `-0.2798` n `13`; crypto_alt avg `0.0745` n `239`; crypto_major avg `-1.2264` n `8`; equity avg `-2.2872` n `162`; fx avg `-0.0708` n `6`; index avg `-0.1667` n `27`; metal avg `-0.27` n `20`; unknown avg `1.9578` n `1091`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
