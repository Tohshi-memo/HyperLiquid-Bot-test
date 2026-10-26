# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T14:07:31.964380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1414` n `13`; crypto_alt avg `-0.0713` n `237`; crypto_major avg `0.0037` n `8`; equity avg `-0.4636` n `152`; fx avg `0.0014` n `6`; index avg `-0.0613` n `26`; metal avg `0.0133` n `20`; unknown avg `0.291` n `1239`
- 1h: commodity avg `-0.1289` n `13`; crypto_alt avg `-0.3265` n `237`; crypto_major avg `-0.3962` n `8`; equity avg `-0.752` n `152`; fx avg `-0.0101` n `6`; index avg `-0.0394` n `26`; metal avg `-0.1435` n `20`; unknown avg `1.9564` n `1234`
- 4h: commodity avg `-0.0734` n `13`; crypto_alt avg `-0.2205` n `237`; crypto_major avg `-0.4238` n `8`; equity avg `-0.5506` n `152`; fx avg `-0.0113` n `6`; index avg `-0.0242` n `26`; metal avg `-0.2054` n `20`; unknown avg `2.6136` n `1216`
- 24h: commodity avg `-0.4079` n `13`; crypto_alt avg `0.0898` n `237`; crypto_major avg `-0.1508` n `8`; equity avg `-0.816` n `152`; fx avg `0.0156` n `6`; index avg `-0.0092` n `26`; metal avg `-0.051` n `20`; unknown avg `-0.1389` n `959`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2342`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
