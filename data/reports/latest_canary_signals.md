# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T12:16:11.946152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `0.0433` n `230`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0355` n `120`; fx avg `0.0024` n `6`; index avg `0.0052` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0055` n `792`
- 1h: commodity avg `0.1032` n `12`; crypto_alt avg `0.026` n `230`; crypto_major avg `-0.0094` n `8`; equity avg `-0.2687` n `120`; fx avg `-0.0117` n `6`; index avg `0.0013` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0005` n `792`
- 4h: commodity avg `0.1916` n `12`; crypto_alt avg `0.2195` n `230`; crypto_major avg `0.279` n `8`; equity avg `-0.7642` n `120`; fx avg `-0.0508` n `6`; index avg `-0.0426` n `25`; metal avg `0.0864` n `20`; unknown avg `0.0828` n `789`
- 24h: commodity avg `0.4146` n `12`; crypto_alt avg `0.3468` n `230`; crypto_major avg `0.3064` n `8`; equity avg `-2.0953` n `120`; fx avg `-0.2127` n `6`; index avg `-0.2284` n `25`; metal avg `-0.4448` n `20`; unknown avg `-0.0617` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
