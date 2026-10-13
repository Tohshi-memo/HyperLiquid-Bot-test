# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T14:52:32.794659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `13`; crypto_alt avg `0.0738` n `235`; crypto_major avg `0.0616` n `8`; equity avg `-0.1966` n `151`; fx avg `0.0087` n `6`; index avg `-0.0411` n `26`; metal avg `0.0416` n `20`; unknown avg `0.6887` n `1135`
- 1h: commodity avg `0.1749` n `13`; crypto_alt avg `0.4103` n `235`; crypto_major avg `0.4645` n `8`; equity avg `-0.0861` n `151`; fx avg `-0.0012` n `6`; index avg `-0.0385` n `26`; metal avg `-0.0422` n `20`; unknown avg `0.2232` n `1109`
- 4h: commodity avg `0.8011` n `13`; crypto_alt avg `0.5795` n `235`; crypto_major avg `0.6275` n `8`; equity avg `-0.7906` n `151`; fx avg `0.0563` n `6`; index avg `-0.0175` n `26`; metal avg `-0.2249` n `20`; unknown avg `0.1359` n `1095`
- 24h: commodity avg `0.3606` n `13`; crypto_alt avg `-1.755` n `235`; crypto_major avg `-0.3916` n `8`; equity avg `-1.6147` n `151`; fx avg `0.1095` n `6`; index avg `-0.2366` n `26`; metal avg `-0.1266` n `20`; unknown avg `0.2517` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1615`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1464`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1364`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0859`, n `666`, weak_sample_signal
