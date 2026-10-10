# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T03:37:28.177003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `13`; crypto_alt avg `-0.1046` n `235`; crypto_major avg `-0.0911` n `8`; equity avg `-0.0159` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0012` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.113` n `1116`
- 1h: commodity avg `0.0344` n `13`; crypto_alt avg `-0.1858` n `235`; crypto_major avg `-0.2091` n `8`; equity avg `-0.0002` n `150`; fx avg `-0.0023` n `6`; index avg `0.0024` n `26`; metal avg `0.0182` n `20`; unknown avg `-0.1047` n `1114`
- 4h: commodity avg `0.0105` n `13`; crypto_alt avg `0.7138` n `235`; crypto_major avg `0.2018` n `8`; equity avg `0.0878` n `150`; fx avg `0.0039` n `6`; index avg `0.0288` n `26`; metal avg `0.0389` n `20`; unknown avg `-0.0321` n `1108`
- 24h: commodity avg `0.0124` n `13`; crypto_alt avg `1.9865` n `235`; crypto_major avg `0.0748` n `8`; equity avg `0.5318` n `150`; fx avg `-0.0217` n `6`; index avg `0.0754` n `26`; metal avg `0.1925` n `20`; unknown avg `12.8488` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
