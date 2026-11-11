# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T11:22:23.378599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0597` n `13`; crypto_alt avg `0.1096` n `239`; crypto_major avg `0.0997` n `8`; equity avg `0.147` n `161`; fx avg `-0.0` n `6`; index avg `0.0213` n `27`; metal avg `0.0315` n `20`; unknown avg `0.347` n `1261`
- 1h: commodity avg `-0.0694` n `13`; crypto_alt avg `-0.0496` n `239`; crypto_major avg `0.0883` n `8`; equity avg `0.3388` n `161`; fx avg `-0.0082` n `6`; index avg `0.0561` n `27`; metal avg `0.0207` n `20`; unknown avg `0.0782` n `1253`
- 4h: commodity avg `0.2647` n `13`; crypto_alt avg `0.3475` n `239`; crypto_major avg `0.417` n `8`; equity avg `0.8519` n `161`; fx avg `-0.0452` n `6`; index avg `0.0383` n `27`; metal avg `0.083` n `20`; unknown avg `40.8809` n `1223`
- 24h: commodity avg `0.5639` n `13`; crypto_alt avg `-0.2786` n `239`; crypto_major avg `-0.9097` n `8`; equity avg `2.8569` n `161`; fx avg `-0.218` n `6`; index avg `0.2706` n `27`; metal avg `0.3355` n `20`; unknown avg `1.8293` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
