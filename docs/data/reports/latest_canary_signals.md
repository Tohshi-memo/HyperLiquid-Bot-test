# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T20:52:25.247315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.0502` n `230`; crypto_major avg `-0.1349` n `8`; equity avg `-0.0634` n `102`; fx avg `0.0024` n `6`; index avg `-0.0189` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.005` n `774`
- 1h: commodity avg `-0.0304` n `12`; crypto_alt avg `0.1616` n `230`; crypto_major avg `-0.052` n `8`; equity avg `0.1717` n `102`; fx avg `-0.0016` n `6`; index avg `0.0243` n `25`; metal avg `-0.0598` n `20`; unknown avg `0.0646` n `774`
- 4h: commodity avg `-0.2855` n `12`; crypto_alt avg `0.0744` n `230`; crypto_major avg `-0.048` n `8`; equity avg `0.6722` n `102`; fx avg `-0.012` n `6`; index avg `0.1542` n `25`; metal avg `-0.0372` n `20`; unknown avg `95.5655` n `774`
- 24h: commodity avg `-1.0681` n `12`; crypto_alt avg `-0.7558` n `230`; crypto_major avg `-0.2306` n `8`; equity avg `-0.9837` n `102`; fx avg `-0.0359` n `6`; index avg `-0.3235` n `25`; metal avg `0.1955` n `20`; unknown avg `97.6623` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
