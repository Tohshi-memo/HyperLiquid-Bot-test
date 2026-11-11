# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T12:52:26.493885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `13`; crypto_alt avg `0.1363` n `239`; crypto_major avg `0.2173` n `8`; equity avg `-0.0998` n `161`; fx avg `0.0124` n `6`; index avg `-0.0087` n `27`; metal avg `0.0422` n `20`; unknown avg `-0.1049` n `1261`
- 1h: commodity avg `0.1302` n `13`; crypto_alt avg `0.0277` n `239`; crypto_major avg `0.0331` n `8`; equity avg `0.2063` n `161`; fx avg `0.0327` n `6`; index avg `0.0166` n `27`; metal avg `0.0407` n `20`; unknown avg `19.1474` n `1249`
- 4h: commodity avg `0.3816` n `13`; crypto_alt avg `0.4557` n `239`; crypto_major avg `0.4556` n `8`; equity avg `0.5794` n `161`; fx avg `0.0416` n `6`; index avg `0.0275` n `27`; metal avg `0.0565` n `20`; unknown avg `0.253` n `1233`
- 24h: commodity avg `0.9819` n `13`; crypto_alt avg `-0.398` n `239`; crypto_major avg `-1.0131` n `8`; equity avg `3.5799` n `161`; fx avg `-0.1707` n `6`; index avg `0.3139` n `27`; metal avg `0.2941` n `20`; unknown avg `1.4305` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2808`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
