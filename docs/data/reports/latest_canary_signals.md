# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T21:37:26.305058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `-0.0335` n `239`; crypto_major avg `-0.0647` n `8`; equity avg `0.0619` n `166`; fx avg `0.0518` n `6`; index avg `0.0134` n `27`; metal avg `0.0263` n `20`; unknown avg `170.8266` n `1264`
- 1h: commodity avg `-0.0369` n `13`; crypto_alt avg `0.0713` n `239`; crypto_major avg `0.309` n `8`; equity avg `0.1067` n `166`; fx avg `0.0485` n `6`; index avg `0.0027` n `27`; metal avg `0.0088` n `20`; unknown avg `161.5065` n `1244`
- 4h: commodity avg `-0.0488` n `13`; crypto_alt avg `-0.3041` n `239`; crypto_major avg `-0.1361` n `8`; equity avg `0.0556` n `166`; fx avg `0.0509` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0801` n `20`; unknown avg `0.9197` n `1219`
- 24h: commodity avg `-0.1516` n `13`; crypto_alt avg `0.9023` n `239`; crypto_major avg `0.7379` n `8`; equity avg `0.8846` n `166`; fx avg `0.0535` n `6`; index avg `0.09` n `27`; metal avg `-0.0193` n `20`; unknown avg `193.7463` n `1062`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
