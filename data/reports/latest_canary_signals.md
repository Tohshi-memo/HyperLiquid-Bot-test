# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T04:37:25.117590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.2052` n `230`; crypto_major avg `-0.1429` n `8`; equity avg `-0.0583` n `102`; fx avg `0.001` n `6`; index avg `-0.0031` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0043` n `774`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.1447` n `230`; crypto_major avg `-0.0764` n `8`; equity avg `-0.2112` n `102`; fx avg `0.0172` n `6`; index avg `-0.0396` n `25`; metal avg `-0.0135` n `20`; unknown avg `-0.0575` n `774`
- 4h: commodity avg `-0.06` n `12`; crypto_alt avg `-0.4593` n `230`; crypto_major avg `-0.4652` n `8`; equity avg `-1.1263` n `102`; fx avg `-0.0422` n `6`; index avg `-0.1834` n `25`; metal avg `-0.1785` n `20`; unknown avg `0.1582` n `774`
- 24h: commodity avg `-0.7267` n `12`; crypto_alt avg `-4.0456` n `230`; crypto_major avg `-3.5831` n `8`; equity avg `-3.4251` n `102`; fx avg `-0.1194` n `6`; index avg `-0.7382` n `25`; metal avg `-0.2702` n `20`; unknown avg `1161.8614` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
