# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T10:37:18.368076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `12`; crypto_alt avg `0.0975` n `228`; crypto_major avg `0.0968` n `8`; equity avg `-0.1663` n `66`; fx avg `0.0129` n `5`; index avg `-0.0905` n `23`; metal avg `-0.0641` n `18`; unknown avg `-0.0932` n `383`
- 1h: commodity avg `0.1824` n `12`; crypto_alt avg `-0.4178` n `228`; crypto_major avg `-0.1193` n `8`; equity avg `-0.4187` n `66`; fx avg `0.0362` n `5`; index avg `-0.1986` n `23`; metal avg `-0.1744` n `18`; unknown avg `-0.1258` n `383`
- 4h: commodity avg `-0.1556` n `12`; crypto_alt avg `-0.4877` n `228`; crypto_major avg `-0.1188` n `8`; equity avg `0.3478` n `66`; fx avg `0.0398` n `5`; index avg `0.1439` n `23`; metal avg `0.1801` n `18`; unknown avg `-0.4441` n `383`
- 24h: commodity avg `0.8801` n `12`; crypto_alt avg `-3.5831` n `228`; crypto_major avg `-2.0882` n `8`; equity avg `-0.1663` n `65`; fx avg `0.097` n `5`; index avg `0.0066` n `23`; metal avg `-0.1381` n `18`; unknown avg `-0.7925` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
