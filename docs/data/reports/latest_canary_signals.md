# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T23:37:27.545495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `13`; crypto_alt avg `-0.0464` n `238`; crypto_major avg `0.014` n `8`; equity avg `-0.2174` n `155`; fx avg `-0.006` n `6`; index avg `-0.0466` n `27`; metal avg `-0.0086` n `20`; unknown avg `0.2435` n `1236`
- 1h: commodity avg `0.0002` n `13`; crypto_alt avg `-0.2042` n `238`; crypto_major avg `-0.0292` n `8`; equity avg `0.0028` n `155`; fx avg `-0.0033` n `6`; index avg `0.0123` n `27`; metal avg `0.0328` n `20`; unknown avg `2.2005` n `1180`
- 4h: commodity avg `-0.2789` n `13`; crypto_alt avg `0.0495` n `238`; crypto_major avg `0.13` n `8`; equity avg `-0.9075` n `155`; fx avg `-0.0178` n `6`; index avg `-0.1296` n `27`; metal avg `0.0613` n `20`; unknown avg `2.9609` n `1064`
- 24h: commodity avg `0.108` n `13`; crypto_alt avg `0.5192` n `238`; crypto_major avg `0.5746` n `8`; equity avg `0.7303` n `154`; fx avg `0.2385` n `6`; index avg `0.1112` n `27`; metal avg `-0.1283` n `20`; unknown avg `25.8215` n `1010`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
