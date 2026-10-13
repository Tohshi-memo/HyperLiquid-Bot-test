# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T17:52:40.445299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0406` n `13`; crypto_alt avg `-0.2559` n `235`; crypto_major avg `-0.2536` n `8`; equity avg `-0.1588` n `151`; fx avg `0.0052` n `6`; index avg `-0.0342` n `26`; metal avg `-0.1025` n `20`; unknown avg `-0.2481` n `1135`
- 1h: commodity avg `0.0562` n `13`; crypto_alt avg `-0.6041` n `235`; crypto_major avg `-0.5465` n `8`; equity avg `-0.3858` n `151`; fx avg `0.0182` n `6`; index avg `-0.0595` n `26`; metal avg `-0.086` n `20`; unknown avg `-0.0728` n `1133`
- 4h: commodity avg `0.4104` n `13`; crypto_alt avg `-0.214` n `235`; crypto_major avg `-0.2266` n `8`; equity avg `0.0365` n `151`; fx avg `-0.001` n `6`; index avg `-0.0423` n `26`; metal avg `-0.2645` n `20`; unknown avg `0.3429` n `1099`
- 24h: commodity avg `0.5422` n `13`; crypto_alt avg `-1.9929` n `235`; crypto_major avg `-0.7111` n `8`; equity avg `-1.1796` n `151`; fx avg `0.1619` n `6`; index avg `-0.2361` n `26`; metal avg `-0.3503` n `20`; unknown avg `0.1857` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1636`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1481`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0911`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0898`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
