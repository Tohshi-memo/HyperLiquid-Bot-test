# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T01:04:46.824962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.1661` n `230`; crypto_major avg `-0.0699` n `8`; equity avg `-0.1476` n `102`; fx avg `-0.0114` n `6`; index avg `-0.0235` n `25`; metal avg `-0.1147` n `20`; unknown avg `0.2054` n `777`
- 1h: commodity avg `0.1004` n `12`; crypto_alt avg `-0.316` n `230`; crypto_major avg `-0.0822` n `8`; equity avg `-0.6635` n `102`; fx avg `-0.0352` n `6`; index avg `-0.0829` n `25`; metal avg `-0.1231` n `20`; unknown avg `0.101` n `777`
- 4h: commodity avg `0.6361` n `12`; crypto_alt avg `-0.1495` n `230`; crypto_major avg `0.0966` n `8`; equity avg `0.1866` n `102`; fx avg `0.0038` n `6`; index avg `0.1109` n `25`; metal avg `-0.0971` n `20`; unknown avg `0.0946` n `776`
- 24h: commodity avg `-0.12` n `12`; crypto_alt avg `0.7329` n `230`; crypto_major avg `1.2329` n `8`; equity avg `-1.0471` n `102`; fx avg `-0.1573` n `6`; index avg `0.0048` n `25`; metal avg `-0.2599` n `20`; unknown avg `0.4011` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
