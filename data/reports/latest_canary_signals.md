# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T06:22:27.721220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `13`; crypto_alt avg `-0.0735` n `235`; crypto_major avg `-0.045` n `8`; equity avg `-0.0063` n `150`; fx avg `0.0` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.0358` n `1116`
- 1h: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.1896` n `235`; crypto_major avg `0.002` n `8`; equity avg `-0.0417` n `150`; fx avg `0.0007` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.0169` n `1098`
- 4h: commodity avg `0.0893` n `13`; crypto_alt avg `0.1443` n `235`; crypto_major avg `0.1214` n `8`; equity avg `0.0242` n `150`; fx avg `0.008` n `6`; index avg `0.0158` n `26`; metal avg `-0.0102` n `20`; unknown avg `-0.1476` n `1092`
- 24h: commodity avg `0.02` n `13`; crypto_alt avg `1.6355` n `235`; crypto_major avg `0.1036` n `8`; equity avg `-0.0292` n `150`; fx avg `-0.0419` n `6`; index avg `0.0349` n `26`; metal avg `0.061` n `20`; unknown avg `667.7409` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
