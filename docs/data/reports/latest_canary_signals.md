# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T12:37:30.875284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.3124` n `230`; crypto_major avg `-0.2993` n `8`; equity avg `-0.0274` n `121`; fx avg `-0.0028` n `6`; index avg `0.0053` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0827` n `794`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `0.3193` n `230`; crypto_major avg `0.5945` n `8`; equity avg `0.051` n `121`; fx avg `-0.0107` n `6`; index avg `0.0087` n `25`; metal avg `0.0158` n `20`; unknown avg `0.1003` n `794`
- 4h: commodity avg `-0.024` n `12`; crypto_alt avg `0.2242` n `230`; crypto_major avg `0.5276` n `8`; equity avg `-0.0032` n `121`; fx avg `0.0205` n `6`; index avg `0.0115` n `25`; metal avg `0.0366` n `20`; unknown avg `0.3243` n `794`
- 24h: commodity avg `0.026` n `12`; crypto_alt avg `1.6493` n `230`; crypto_major avg `4.1764` n `8`; equity avg `-0.9363` n `121`; fx avg `0.0424` n `6`; index avg `-0.1283` n `25`; metal avg `-0.0416` n `20`; unknown avg `1.5105` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
