# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T08:07:37.867199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `13`; crypto_alt avg `0.0461` n `239`; crypto_major avg `0.0538` n `8`; equity avg `0.1681` n `161`; fx avg `0.0168` n `6`; index avg `0.0174` n `27`; metal avg `0.02` n `20`; unknown avg `17.5418` n `1240`
- 1h: commodity avg `0.0901` n `13`; crypto_alt avg `-0.0181` n `239`; crypto_major avg `0.2083` n `8`; equity avg `0.021` n `161`; fx avg `0.0486` n `6`; index avg `-0.0062` n `27`; metal avg `0.0416` n `20`; unknown avg `15.5056` n `1238`
- 4h: commodity avg `0.3507` n `13`; crypto_alt avg `-0.4425` n `239`; crypto_major avg `-0.4096` n `8`; equity avg `-0.6354` n `161`; fx avg `0.0878` n `6`; index avg `-0.1206` n `27`; metal avg `-0.0543` n `20`; unknown avg `15.9176` n `1198`
- 24h: commodity avg `0.387` n `13`; crypto_alt avg `-1.6024` n `239`; crypto_major avg `-0.8518` n `8`; equity avg `-0.6934` n `161`; fx avg `-0.0969` n `6`; index avg `-0.0971` n `27`; metal avg `-0.5955` n `20`; unknown avg `17.1087` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
