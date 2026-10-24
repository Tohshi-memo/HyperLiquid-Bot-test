# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T17:52:28.137083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `13`; crypto_alt avg `0.3466` n `237`; crypto_major avg `0.2715` n `8`; equity avg `0.0586` n `152`; fx avg `0.0065` n `6`; index avg `0.0025` n `26`; metal avg `0.0035` n `20`; unknown avg `0.1588` n `1231`
- 1h: commodity avg `0.0251` n `13`; crypto_alt avg `-0.0379` n `237`; crypto_major avg `0.0883` n `8`; equity avg `-0.0099` n `152`; fx avg `-0.0048` n `6`; index avg `0.0013` n `26`; metal avg `0.0046` n `20`; unknown avg `0.1917` n `1215`
- 4h: commodity avg `0.0237` n `13`; crypto_alt avg `-1.1239` n `237`; crypto_major avg `-0.7764` n `8`; equity avg `-0.3091` n `152`; fx avg `-0.0232` n `6`; index avg `-0.0445` n `26`; metal avg `-0.11` n `20`; unknown avg `0.2993` n `1198`
- 24h: commodity avg `0.1988` n `13`; crypto_alt avg `-3.904` n `237`; crypto_major avg `-2.6433` n `8`; equity avg `-0.8119` n `152`; fx avg `-0.0402` n `6`; index avg `-0.0828` n `26`; metal avg `-0.1927` n `20`; unknown avg `-0.3035` n `1045`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
