# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T21:37:31.411573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0153` n `13`; crypto_alt avg `0.5737` n `239`; crypto_major avg `0.5548` n `8`; equity avg `0.0168` n `166`; fx avg `0.0012` n `6`; index avg `0.0014` n `27`; metal avg `0.0397` n `20`; unknown avg `2.9837` n `1262`
- 1h: commodity avg `-0.003` n `13`; crypto_alt avg `0.8078` n `239`; crypto_major avg `0.9701` n `8`; equity avg `0.7552` n `166`; fx avg `0.0022` n `6`; index avg `0.097` n `27`; metal avg `0.1046` n `20`; unknown avg `264.6651` n `1230`
- 4h: commodity avg `0.5331` n `13`; crypto_alt avg `0.3707` n `239`; crypto_major avg `-0.2033` n `8`; equity avg `-0.6584` n `166`; fx avg `-0.0365` n `6`; index avg `-0.1678` n `27`; metal avg `-0.0331` n `20`; unknown avg `2.455` n `1218`
- 24h: commodity avg `0.2614` n `13`; crypto_alt avg `-5.0516` n `239`; crypto_major avg `-5.4632` n `8`; equity avg `-6.3109` n `166`; fx avg `0.0169` n `6`; index avg `-0.7141` n `27`; metal avg `-0.8469` n `20`; unknown avg `19.4873` n `1135`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
