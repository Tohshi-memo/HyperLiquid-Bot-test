# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T07:05:21.941610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `0.5117` n `230`; crypto_major avg `0.5633` n `8`; equity avg `-0.026` n `121`; fx avg `-0.007` n `6`; index avg `0.0088` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.6029` n `794`
- 1h: commodity avg `-0.0173` n `12`; crypto_alt avg `1.4159` n `230`; crypto_major avg `1.3898` n `8`; equity avg `0.1302` n `121`; fx avg `-0.0103` n `6`; index avg `0.0193` n `25`; metal avg `0.003` n `20`; unknown avg `0.7465` n `794`
- 4h: commodity avg `0.0652` n `12`; crypto_alt avg `-2.2318` n `230`; crypto_major avg `-0.7239` n `8`; equity avg `-0.3559` n `121`; fx avg `0.0071` n `6`; index avg `-0.033` n `25`; metal avg `-0.1201` n `20`; unknown avg `0.5622` n `777`
- 24h: commodity avg `0.1834` n `12`; crypto_alt avg `6.96` n `230`; crypto_major avg `7.3569` n `8`; equity avg `-0.4173` n `121`; fx avg `0.012` n `6`; index avg `-0.0738` n `25`; metal avg `-0.0193` n `20`; unknown avg `1.8987` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
