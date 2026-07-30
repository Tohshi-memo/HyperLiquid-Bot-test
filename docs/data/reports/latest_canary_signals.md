# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T09:56:02.798918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0531` n `12`; crypto_alt avg `-0.0869` n `230`; crypto_major avg `-0.0982` n `8`; equity avg `-0.0695` n `102`; fx avg `-0.0053` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0235` n `20`; unknown avg `-0.0199` n `779`
- 1h: commodity avg `-0.114` n `12`; crypto_alt avg `-0.0298` n `230`; crypto_major avg `0.1788` n `8`; equity avg `0.3773` n `102`; fx avg `-0.0168` n `6`; index avg `0.0477` n `25`; metal avg `0.119` n `20`; unknown avg `-0.0244` n `771`
- 4h: commodity avg `-0.1532` n `12`; crypto_alt avg `0.1785` n `230`; crypto_major avg `0.5201` n `8`; equity avg `0.4668` n `102`; fx avg `0.0069` n `6`; index avg `0.0261` n `25`; metal avg `0.3559` n `20`; unknown avg `-0.0093` n `739`
- 24h: commodity avg `0.6557` n `12`; crypto_alt avg `-0.4033` n `230`; crypto_major avg `-0.3565` n `8`; equity avg `-3.3925` n `102`; fx avg `0.0015` n `6`; index avg `-0.4878` n `25`; metal avg `0.2923` n `20`; unknown avg `-0.1798` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
