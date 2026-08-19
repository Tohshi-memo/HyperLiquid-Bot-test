# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T09:37:26.043513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.1184` n `230`; crypto_major avg `-0.0941` n `8`; equity avg `-0.0463` n `120`; fx avg `-0.0126` n `6`; index avg `-0.0012` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0253` n `791`
- 1h: commodity avg `0.1053` n `12`; crypto_alt avg `-0.2542` n `230`; crypto_major avg `-0.094` n `8`; equity avg `-0.2428` n `120`; fx avg `0.0032` n `6`; index avg `-0.0391` n `25`; metal avg `-0.0321` n `20`; unknown avg `0.0212` n `789`
- 4h: commodity avg `0.0417` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `0.1504` n `8`; equity avg `0.9692` n `120`; fx avg `0.0056` n `6`; index avg `0.2132` n `25`; metal avg `0.1075` n `20`; unknown avg `0.0062` n `757`
- 24h: commodity avg `0.4098` n `12`; crypto_alt avg `0.1466` n `230`; crypto_major avg `0.3743` n `8`; equity avg `-1.4197` n `120`; fx avg `-0.189` n `6`; index avg `-0.1568` n `25`; metal avg `-0.4555` n `20`; unknown avg `-0.2236` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
