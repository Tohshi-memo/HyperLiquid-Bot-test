# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T00:10:16.315336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `-0.1126` n `239`; crypto_major avg `-0.2283` n `8`; equity avg `-0.2717` n `168`; fx avg `0.0311` n `6`; index avg `-0.0431` n `27`; metal avg `-0.039` n `20`; unknown avg `39.9317` n `1247`
- 1h: commodity avg `0.0211` n `13`; crypto_alt avg `-0.3015` n `239`; crypto_major avg `-0.597` n `8`; equity avg `-0.9704` n `168`; fx avg `0.055` n `6`; index avg `-0.1052` n `27`; metal avg `-0.1008` n `20`; unknown avg `87.2365` n `1237`
- 4h: commodity avg `0.0635` n `13`; crypto_alt avg `0.0312` n `239`; crypto_major avg `0.1148` n `8`; equity avg `-0.13` n `168`; fx avg `0.0339` n `6`; index avg `-0.0292` n `27`; metal avg `-0.0231` n `20`; unknown avg `1.0298` n `1163`
- 24h: commodity avg `0.5562` n `13`; crypto_alt avg `-2.9657` n `239`; crypto_major avg `-2.4671` n `8`; equity avg `-4.5025` n `167`; fx avg `0.2915` n `6`; index avg `-0.3346` n `27`; metal avg `-1.1383` n `20`; unknown avg `657.5895` n `1057`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
