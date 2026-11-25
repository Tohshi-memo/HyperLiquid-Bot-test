# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T04:52:29.792802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `0.0257` n `239`; crypto_major avg `-0.1539` n `8`; equity avg `-0.1465` n `168`; fx avg `-0.005` n `6`; index avg `-0.0052` n `27`; metal avg `0.0184` n `20`; unknown avg `0.154` n `1263`
- 1h: commodity avg `0.0477` n `13`; crypto_alt avg `0.3501` n `239`; crypto_major avg `-0.3083` n `8`; equity avg `-0.286` n `168`; fx avg `-0.0041` n `6`; index avg `0.0039` n `27`; metal avg `0.0046` n `20`; unknown avg `0.1769` n `1249`
- 4h: commodity avg `-0.2462` n `13`; crypto_alt avg `0.1916` n `239`; crypto_major avg `-0.8317` n `8`; equity avg `-1.0153` n `168`; fx avg `-0.0646` n `6`; index avg `-0.0748` n `27`; metal avg `-0.0924` n `20`; unknown avg `0.7962` n `1241`
- 24h: commodity avg `0.5577` n `13`; crypto_alt avg `-2.9701` n `239`; crypto_major avg `-3.1583` n `8`; equity avg `-5.1864` n `167`; fx avg `0.1619` n `6`; index avg `-0.4965` n `27`; metal avg `-0.9265` n `20`; unknown avg `507.9297` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
