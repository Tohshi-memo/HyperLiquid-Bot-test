# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T12:52:31.403107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0412` n `13`; crypto_alt avg `0.0404` n `235`; crypto_major avg `0.0343` n `8`; equity avg `0.002` n `150`; fx avg `-0.0001` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.5317` n `1117`
- 1h: commodity avg `0.0897` n `13`; crypto_alt avg `0.0929` n `235`; crypto_major avg `-0.0397` n `8`; equity avg `0.0035` n `150`; fx avg `0.0021` n `6`; index avg `-0.0027` n `26`; metal avg `0.0` n `20`; unknown avg `0.1248` n `1109`
- 4h: commodity avg `-0.1511` n `13`; crypto_alt avg `-0.1067` n `235`; crypto_major avg `-0.1547` n `8`; equity avg `0.0265` n `150`; fx avg `0.0069` n `6`; index avg `0.0034` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.3717` n `1109`
- 24h: commodity avg `-0.2551` n `13`; crypto_alt avg `1.983` n `235`; crypto_major avg `0.1878` n `8`; equity avg `-0.0721` n `150`; fx avg `0.0397` n `6`; index avg `0.0238` n `26`; metal avg `0.1316` n `20`; unknown avg `632.2395` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
