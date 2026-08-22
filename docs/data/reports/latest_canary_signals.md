# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T15:37:29.958157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.4678` n `230`; crypto_major avg `0.3752` n `8`; equity avg `0.0043` n `121`; fx avg `0.003` n `6`; index avg `0.0` n `25`; metal avg `0.0062` n `20`; unknown avg `0.189` n `794`
- 1h: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.2249` n `230`; crypto_major avg `-0.0775` n `8`; equity avg `-0.0873` n `121`; fx avg `0.0041` n `6`; index avg `0.0067` n `25`; metal avg `0.0076` n `20`; unknown avg `0.1112` n `794`
- 4h: commodity avg `-0.0733` n `12`; crypto_alt avg `-0.6462` n `230`; crypto_major avg `-0.3938` n `8`; equity avg `-0.0479` n `121`; fx avg `-0.0244` n `6`; index avg `-0.0034` n `25`; metal avg `0.0264` n `20`; unknown avg `0.143` n `794`
- 24h: commodity avg `-0.1087` n `12`; crypto_alt avg `-0.0555` n `230`; crypto_major avg `2.0029` n `8`; equity avg `-0.566` n `121`; fx avg `0.0565` n `6`; index avg `-0.0823` n `25`; metal avg `-0.0764` n `20`; unknown avg `1.835` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
