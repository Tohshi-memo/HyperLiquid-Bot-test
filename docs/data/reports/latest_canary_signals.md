# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T23:22:27.750859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.1011` n `230`; crypto_major avg `-0.1366` n `8`; equity avg `0.0132` n `121`; fx avg `0.0082` n `6`; index avg `0.0077` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0041` n `794`
- 1h: commodity avg `0.0238` n `12`; crypto_alt avg `0.1633` n `230`; crypto_major avg `-0.2368` n `8`; equity avg `0.0113` n `121`; fx avg `0.0351` n `6`; index avg `0.0082` n `25`; metal avg `-0.0087` n `20`; unknown avg `0.1365` n `794`
- 4h: commodity avg `0.1116` n `12`; crypto_alt avg `-0.9252` n `230`; crypto_major avg `-0.6094` n `8`; equity avg `0.0788` n `121`; fx avg `0.046` n `6`; index avg `0.0071` n `25`; metal avg `0.0083` n `20`; unknown avg `0.2427` n `794`
- 24h: commodity avg `0.0701` n `12`; crypto_alt avg `-2.4715` n `230`; crypto_major avg `-0.9237` n `8`; equity avg `-0.3873` n `121`; fx avg `0.1081` n `6`; index avg `-0.0611` n `25`; metal avg `-0.0775` n `20`; unknown avg `2.9803` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
