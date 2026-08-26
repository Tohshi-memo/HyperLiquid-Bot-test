# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T00:52:30.486660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0502` n `12`; crypto_alt avg `0.4626` n `231`; crypto_major avg `0.3835` n `8`; equity avg `-0.0977` n `122`; fx avg `-0.0108` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.0498` n `796`
- 1h: commodity avg `-0.0653` n `12`; crypto_alt avg `0.5895` n `231`; crypto_major avg `0.3491` n `8`; equity avg `-0.3471` n `122`; fx avg `0.0161` n `6`; index avg `-0.0649` n `25`; metal avg `-0.0607` n `20`; unknown avg `0.0198` n `796`
- 4h: commodity avg `-0.0462` n `12`; crypto_alt avg `0.554` n `231`; crypto_major avg `0.2225` n `8`; equity avg `-0.4632` n `122`; fx avg `0.0168` n `6`; index avg `-0.1443` n `25`; metal avg `-0.0804` n `20`; unknown avg `-0.0196` n `795`
- 24h: commodity avg `-0.7153` n `12`; crypto_alt avg `-2.6538` n `231`; crypto_major avg `-2.3764` n `8`; equity avg `1.4616` n `122`; fx avg `0.0373` n `6`; index avg `0.1512` n `25`; metal avg `-0.3005` n `20`; unknown avg `-0.4122` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
