# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T06:22:32.373840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `13`; crypto_alt avg `-0.2549` n `239`; crypto_major avg `-0.0969` n `8`; equity avg `0.0608` n `161`; fx avg `-0.0058` n `6`; index avg `0.0113` n `27`; metal avg `0.0233` n `20`; unknown avg `0.0264` n `1255`
- 1h: commodity avg `0.0959` n `13`; crypto_alt avg `-0.5277` n `239`; crypto_major avg `-0.0527` n `8`; equity avg `0.2367` n `161`; fx avg `-0.0099` n `6`; index avg `0.009` n `27`; metal avg `0.0628` n `20`; unknown avg `-0.0938` n `1223`
- 4h: commodity avg `0.0495` n `13`; crypto_alt avg `0.0863` n `239`; crypto_major avg `0.5813` n `8`; equity avg `1.367` n `161`; fx avg `-0.0621` n `6`; index avg `0.1534` n `27`; metal avg `0.2815` n `20`; unknown avg `3.693` n `1217`
- 24h: commodity avg `0.2971` n `13`; crypto_alt avg `-1.0256` n `239`; crypto_major avg `-2.1769` n `8`; equity avg `1.6397` n `161`; fx avg `-0.1956` n `6`; index avg `0.1986` n `27`; metal avg `-0.1101` n `20`; unknown avg `2.9209` n `1162`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.22`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
