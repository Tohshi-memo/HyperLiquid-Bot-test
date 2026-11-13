# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T10:37:37.762077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0352` n `13`; crypto_alt avg `-0.1195` n `239`; crypto_major avg `-0.0246` n `8`; equity avg `-0.0692` n `162`; fx avg `-0.0091` n `6`; index avg `0.0011` n `27`; metal avg `-0.0212` n `20`; unknown avg `5.162` n `1240`
- 1h: commodity avg `-0.1424` n `13`; crypto_alt avg `0.0573` n `239`; crypto_major avg `0.2359` n `8`; equity avg `0.0136` n `162`; fx avg `-0.018` n `6`; index avg `0.0096` n `27`; metal avg `-0.0649` n `20`; unknown avg `5.2287` n `1206`
- 4h: commodity avg `-0.1412` n `13`; crypto_alt avg `0.4079` n `239`; crypto_major avg `0.7093` n `8`; equity avg `0.3702` n `162`; fx avg `-0.0134` n `6`; index avg `0.0594` n `27`; metal avg `-0.0457` n `20`; unknown avg `6.5417` n `1148`
- 24h: commodity avg `0.5981` n `13`; crypto_alt avg `-1.1919` n `239`; crypto_major avg `-3.0102` n `8`; equity avg `-1.5003` n `162`; fx avg `-0.0452` n `6`; index avg `-0.0006` n `27`; metal avg `-0.4684` n `20`; unknown avg `1.7723` n `1073`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
