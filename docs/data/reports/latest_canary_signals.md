# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T17:37:28.507081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.1031` n `230`; crypto_major avg `0.0622` n `8`; equity avg `-0.0057` n `92`; fx avg `-0.0067` n `6`; index avg `0.0018` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.001` n `765`
- 1h: commodity avg `0.0595` n `12`; crypto_alt avg `0.0768` n `230`; crypto_major avg `0.0442` n `8`; equity avg `0.0071` n `92`; fx avg `-0.0073` n `6`; index avg `-0.0016` n `25`; metal avg `-0.008` n `20`; unknown avg `-0.0973` n `765`
- 4h: commodity avg `0.1306` n `12`; crypto_alt avg `0.0474` n `230`; crypto_major avg `0.3195` n `8`; equity avg `-0.0131` n `92`; fx avg `-0.0039` n `6`; index avg `0.0163` n `25`; metal avg `-0.0247` n `20`; unknown avg `-0.0888` n `759`
- 24h: commodity avg `0.5736` n `12`; crypto_alt avg `-1.2472` n `230`; crypto_major avg `-0.5061` n `8`; equity avg `-0.1662` n `92`; fx avg `0.0098` n `6`; index avg `-0.087` n `25`; metal avg `-0.1126` n `20`; unknown avg `0.1577` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
