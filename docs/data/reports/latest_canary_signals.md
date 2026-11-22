# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T08:52:37.045102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `13`; crypto_alt avg `-0.4821` n `239`; crypto_major avg `-0.5997` n `8`; equity avg `-0.0701` n `166`; fx avg `-0.0141` n `6`; index avg `-0.0087` n `27`; metal avg `-0.0163` n `20`; unknown avg `0.0788` n `1263`
- 1h: commodity avg `0.0093` n `13`; crypto_alt avg `0.7142` n `239`; crypto_major avg `0.8292` n `8`; equity avg `0.5804` n `166`; fx avg `-0.014` n `6`; index avg `0.0563` n `27`; metal avg `0.0411` n `20`; unknown avg `40.6819` n `1245`
- 4h: commodity avg `0.0118` n `13`; crypto_alt avg `0.8533` n `239`; crypto_major avg `0.7636` n `8`; equity avg `0.5635` n `166`; fx avg `-0.0174` n `6`; index avg `0.0597` n `27`; metal avg `0.0535` n `20`; unknown avg `206.6522` n `1213`
- 24h: commodity avg `0.03` n `13`; crypto_alt avg `2.8484` n `239`; crypto_major avg `3.1707` n `8`; equity avg `1.2424` n `166`; fx avg `0.0078` n `6`; index avg `0.1667` n `27`; metal avg `0.0968` n `20`; unknown avg `235.9123` n `1070`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
