# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T22:52:27.297834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.2562` n `230`; crypto_major avg `0.0878` n `8`; equity avg `0.0361` n `121`; fx avg `0.0031` n `6`; index avg `0.0022` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.1462` n `794`
- 1h: commodity avg `0.0165` n `12`; crypto_alt avg `1.174` n `230`; crypto_major avg `0.685` n `8`; equity avg `0.0263` n `121`; fx avg `0.0183` n `6`; index avg `0.003` n `25`; metal avg `-0.0094` n `20`; unknown avg `0.5551` n `794`
- 4h: commodity avg `0.0997` n `12`; crypto_alt avg `-0.3588` n `230`; crypto_major avg `0.0034` n `8`; equity avg `0.1113` n `121`; fx avg `0.034` n `6`; index avg `-0.0028` n `25`; metal avg `0.0117` n `20`; unknown avg `0.377` n `794`
- 24h: commodity avg `0.0542` n `12`; crypto_alt avg `-2.0135` n `230`; crypto_major avg `-0.2356` n `8`; equity avg `-0.4024` n `121`; fx avg `0.0945` n `6`; index avg `-0.0649` n `25`; metal avg `-0.0635` n `20`; unknown avg `1.8761` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
