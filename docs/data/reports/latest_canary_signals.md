# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T00:52:25.471849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `0.2586` n `230`; crypto_major avg `0.5316` n `8`; equity avg `0.0261` n `121`; fx avg `-0.0034` n `6`; index avg `-0.0017` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0212` n `794`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `0.7511` n `230`; crypto_major avg `1.357` n `8`; equity avg `0.1306` n `121`; fx avg `0.0107` n `6`; index avg `0.0037` n `25`; metal avg `0.0115` n `20`; unknown avg `0.4255` n `794`
- 4h: commodity avg `0.0172` n `12`; crypto_alt avg `-0.1987` n `230`; crypto_major avg `0.4254` n `8`; equity avg `0.1722` n `121`; fx avg `0.0342` n `6`; index avg `0.0171` n `25`; metal avg `0.0172` n `20`; unknown avg `0.5059` n `794`
- 24h: commodity avg `0.1139` n `12`; crypto_alt avg `-1.7932` n `230`; crypto_major avg `1.9539` n `8`; equity avg `-0.2437` n `121`; fx avg `0.1165` n `6`; index avg `-0.0552` n `25`; metal avg `-0.0524` n `20`; unknown avg `3.79` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
