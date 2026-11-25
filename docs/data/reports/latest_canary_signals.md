# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T06:52:27.270414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0361` n `13`; crypto_alt avg `-0.1541` n `239`; crypto_major avg `0.0802` n `8`; equity avg `-0.1085` n `168`; fx avg `-0.0078` n `6`; index avg `-0.0189` n `27`; metal avg `-0.0305` n `20`; unknown avg `3.8085` n `1263`
- 1h: commodity avg `-0.1255` n `13`; crypto_alt avg `0.4527` n `239`; crypto_major avg `0.2068` n `8`; equity avg `-0.0478` n `168`; fx avg `-0.0242` n `6`; index avg `-0.0126` n `27`; metal avg `-0.0103` n `20`; unknown avg `226.8058` n `1229`
- 4h: commodity avg `-0.1611` n `13`; crypto_alt avg `1.3271` n `239`; crypto_major avg `0.3432` n `8`; equity avg `-0.2863` n `168`; fx avg `-0.0532` n `6`; index avg `0.0087` n `27`; metal avg `-0.3265` n `20`; unknown avg `206.528` n `1219`
- 24h: commodity avg `0.3337` n `13`; crypto_alt avg `-2.9121` n `239`; crypto_major avg `-3.0621` n `8`; equity avg `-5.6906` n `167`; fx avg `0.0801` n `6`; index avg `-0.5621` n `27`; metal avg `-1.134` n `20`; unknown avg `692.571` n `1027`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
