# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T10:52:38.018672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0682` n `13`; crypto_alt avg `-0.1709` n `239`; crypto_major avg `-0.1378` n `8`; equity avg `-0.0553` n `168`; fx avg `0.0123` n `6`; index avg `-0.0151` n `27`; metal avg `-0.0169` n `20`; unknown avg `0.092` n `1265`
- 1h: commodity avg `-0.2039` n `13`; crypto_alt avg `-0.0262` n `239`; crypto_major avg `0.232` n `8`; equity avg `0.1335` n `168`; fx avg `0.0265` n `6`; index avg `-0.0145` n `27`; metal avg `-0.0063` n `20`; unknown avg `-0.026` n `1259`
- 4h: commodity avg `0.0993` n `13`; crypto_alt avg `-1.1464` n `239`; crypto_major avg `-1.1271` n `8`; equity avg `-1.4764` n `168`; fx avg `0.0154` n `6`; index avg `-0.177` n `27`; metal avg `0.0127` n `20`; unknown avg `0.2955` n `1235`
- 24h: commodity avg `0.2409` n `13`; crypto_alt avg `-1.8115` n `239`; crypto_major avg `-2.2781` n `8`; equity avg `-4.3027` n `167`; fx avg `0.0254` n `6`; index avg `-0.3662` n `27`; metal avg `-0.8546` n `20`; unknown avg `429.3542` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
