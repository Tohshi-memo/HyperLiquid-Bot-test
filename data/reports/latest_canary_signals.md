# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T18:07:31.325290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `13`; crypto_alt avg `0.1273` n `239`; crypto_major avg `0.2822` n `8`; equity avg `0.0375` n `168`; fx avg `-0.0007` n `6`; index avg `0.0082` n `27`; metal avg `0.0662` n `20`; unknown avg `160.5258` n `1255`
- 1h: commodity avg `0.1132` n `13`; crypto_alt avg `0.6155` n `239`; crypto_major avg `0.5594` n `8`; equity avg `0.3754` n `168`; fx avg `0.0031` n `6`; index avg `0.0532` n `27`; metal avg `0.0171` n `20`; unknown avg `161.4228` n `1247`
- 4h: commodity avg `0.1667` n `13`; crypto_alt avg `-0.3065` n `239`; crypto_major avg `-0.4224` n `8`; equity avg `-1.3037` n `168`; fx avg `0.0417` n `6`; index avg `0.0004` n `27`; metal avg `-0.4995` n `20`; unknown avg `161.6047` n `1237`
- 24h: commodity avg `0.4186` n `13`; crypto_alt avg `-3.6854` n `239`; crypto_major avg `-3.4107` n `8`; equity avg `-4.1589` n `167`; fx avg `0.2782` n `6`; index avg `-0.2537` n `27`; metal avg `-1.1734` n `20`; unknown avg `177.4502` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
