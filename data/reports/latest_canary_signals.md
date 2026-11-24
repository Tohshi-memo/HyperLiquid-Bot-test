# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T23:07:27.722561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.1472` n `239`; crypto_major avg `-0.0001` n `8`; equity avg `0.1258` n `168`; fx avg `-0.0077` n `6`; index avg `0.0267` n `27`; metal avg `0.009` n `20`; unknown avg `-0.2104` n `1239`
- 1h: commodity avg `-0.0116` n `13`; crypto_alt avg `0.2292` n `239`; crypto_major avg `0.243` n `8`; equity avg `0.3747` n `168`; fx avg `0.0052` n `6`; index avg `0.0268` n `27`; metal avg `0.0173` n `20`; unknown avg `0.8652` n `1213`
- 4h: commodity avg `-0.0721` n `13`; crypto_alt avg `-0.2086` n `239`; crypto_major avg `0.3085` n `8`; equity avg `0.4689` n `168`; fx avg `-0.0456` n `6`; index avg `0.0274` n `27`; metal avg `0.0272` n `20`; unknown avg `173.4791` n `1167`
- 24h: commodity avg `0.6116` n `13`; crypto_alt avg `-2.3587` n `239`; crypto_major avg `-2.1078` n `8`; equity avg `-3.9306` n `167`; fx avg `0.2022` n `6`; index avg `-0.2756` n `27`; metal avg `-1.1006` n `20`; unknown avg `427.733` n `1063`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
