# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T13:37:34.440084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0799` n `12`; crypto_alt avg `0.2029` n `230`; crypto_major avg `0.0971` n `8`; equity avg `0.4498` n `109`; fx avg `-0.0023` n `6`; index avg `0.0436` n `25`; metal avg `0.0626` n `20`; unknown avg `1.6849` n `781`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0149` n `230`; crypto_major avg `-0.3329` n `8`; equity avg `-0.1121` n `109`; fx avg `-0.0088` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0863` n `20`; unknown avg `0.6795` n `781`
- 4h: commodity avg `0.1518` n `12`; crypto_alt avg `0.0536` n `230`; crypto_major avg `-0.5722` n `8`; equity avg `-0.2941` n `109`; fx avg `-0.0073` n `6`; index avg `-0.0407` n `25`; metal avg `-0.2297` n `20`; unknown avg `108.6975` n `781`
- 24h: commodity avg `0.0617` n `12`; crypto_alt avg `0.5877` n `230`; crypto_major avg `-0.4762` n `8`; equity avg `-1.7409` n `109`; fx avg `0.0029` n `6`; index avg `-0.4534` n `25`; metal avg `0.3137` n `20`; unknown avg `113.2428` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
