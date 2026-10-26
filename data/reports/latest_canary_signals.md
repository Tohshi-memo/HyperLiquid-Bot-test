# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T11:01:01.853516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `13`; crypto_alt avg `-0.1673` n `237`; crypto_major avg `-0.2078` n `8`; equity avg `-0.1973` n `152`; fx avg `0.0094` n `6`; index avg `-0.0324` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.0567` n `1238`
- 1h: commodity avg `-0.1087` n `13`; crypto_alt avg `-0.1863` n `237`; crypto_major avg `-0.1456` n `8`; equity avg `-0.456` n `152`; fx avg `0.0037` n `6`; index avg `-0.0923` n `26`; metal avg `-0.0685` n `20`; unknown avg `2.7919` n `1240`
- 4h: commodity avg `0.032` n `13`; crypto_alt avg `0.3295` n `237`; crypto_major avg `0.1849` n `8`; equity avg `-0.0714` n `152`; fx avg `0.0153` n `6`; index avg `0.0088` n `26`; metal avg `0.0622` n `20`; unknown avg `13.0375` n `1144`
- 24h: commodity avg `-0.5396` n `13`; crypto_alt avg `0.5168` n `237`; crypto_major avg `0.3208` n `8`; equity avg `-0.4676` n `152`; fx avg `0.0379` n `6`; index avg `-0.0217` n `26`; metal avg `0.1476` n `20`; unknown avg `0.7862` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2607`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2314`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
