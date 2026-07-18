# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T07:37:27.669657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.0059` n `230`; crypto_major avg `0.0197` n `8`; equity avg `0.0141` n `96`; fx avg `-0.0052` n `6`; index avg `-0.0118` n `25`; metal avg `0.0128` n `20`; unknown avg `0.029` n `769`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0788` n `230`; crypto_major avg `0.0784` n `8`; equity avg `0.0766` n `96`; fx avg `0.0078` n `6`; index avg `-0.0302` n `25`; metal avg `0.0258` n `20`; unknown avg `-0.0241` n `769`
- 4h: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.4495` n `230`; crypto_major avg `-0.1494` n `8`; equity avg `-0.1174` n `96`; fx avg `0.0007` n `6`; index avg `-0.0162` n `25`; metal avg `0.0161` n `20`; unknown avg `-0.091` n `737`
- 24h: commodity avg `0.8032` n `12`; crypto_alt avg `-0.0061` n `230`; crypto_major avg `0.7848` n `8`; equity avg `1.3473` n `96`; fx avg `0.0435` n `6`; index avg `0.1444` n `25`; metal avg `0.2886` n `20`; unknown avg `0.2849` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
