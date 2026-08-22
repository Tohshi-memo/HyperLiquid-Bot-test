# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T14:07:36.824098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.8615` n `230`; crypto_major avg `-0.7862` n `8`; equity avg `-0.0269` n `121`; fx avg `-0.0247` n `6`; index avg `-0.0047` n `25`; metal avg `0.004` n `20`; unknown avg `-0.1074` n `794`
- 1h: commodity avg `-0.0757` n `12`; crypto_alt avg `-0.537` n `230`; crypto_major avg `-0.6182` n `8`; equity avg `-0.0207` n `121`; fx avg `-0.0269` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0384` n `794`
- 4h: commodity avg `-0.061` n `12`; crypto_alt avg `-0.0268` n `230`; crypto_major avg `0.2635` n `8`; equity avg `0.0` n `121`; fx avg `-0.0154` n `6`; index avg `-0.0078` n `25`; metal avg `0.0196` n `20`; unknown avg `0.0149` n `794`
- 24h: commodity avg `0.0016` n `12`; crypto_alt avg `0.3429` n `230`; crypto_major avg `2.6914` n `8`; equity avg `-0.6374` n `121`; fx avg `0.0338` n `6`; index avg `-0.0366` n `25`; metal avg `-0.0905` n `20`; unknown avg `0.7187` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
