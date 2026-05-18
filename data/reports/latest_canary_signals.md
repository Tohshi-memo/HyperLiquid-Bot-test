# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T23:37:15.463658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0203` n `228`; crypto_major avg `-0.0157` n `8`; equity avg `-0.0525` n `66`; fx avg `0.0094` n `6`; index avg `-0.0404` n `23`; metal avg `-0.0731` n `18`; unknown avg `0.0538` n `383`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1355` n `228`; crypto_major avg `0.0007` n `8`; equity avg `0.1386` n `66`; fx avg `-0.0021` n `6`; index avg `-0.0145` n `23`; metal avg `0.185` n `18`; unknown avg `-0.1054` n `383`
- 4h: commodity avg `0.0598` n `12`; crypto_alt avg `1.1281` n `228`; crypto_major avg `0.9954` n `8`; equity avg `0.9472` n `66`; fx avg `-0.0066` n `6`; index avg `0.4308` n `23`; metal avg `0.8092` n `18`; unknown avg `0.0124` n `383`
- 24h: commodity avg `0.5672` n `12`; crypto_alt avg `0.1231` n `228`; crypto_major avg `-0.6499` n `8`; equity avg `-0.3254` n `66`; fx avg `0.1724` n `6`; index avg `-0.0058` n `23`; metal avg `1.1245` n `18`; unknown avg `0.2013` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
