# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T23:07:25.734132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.0459` n `230`; crypto_major avg `0.1269` n `8`; equity avg `0.0027` n `121`; fx avg `0.0063` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.0652` n `794`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `0.6119` n `230`; crypto_major avg `0.1376` n `8`; equity avg `-0.0235` n `121`; fx avg `0.0184` n `6`; index avg `-0.006` n `25`; metal avg `-0.0085` n `20`; unknown avg `0.2008` n `794`
- 4h: commodity avg `0.1091` n `12`; crypto_alt avg `-0.9775` n `230`; crypto_major avg `-0.5681` n `8`; equity avg `0.0586` n `121`; fx avg `0.0362` n `6`; index avg `-0.004` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.1563` n `794`
- 24h: commodity avg `0.0565` n `12`; crypto_alt avg `-2.125` n `230`; crypto_major avg `-0.3866` n `8`; equity avg `-0.4357` n `121`; fx avg `0.0999` n `6`; index avg `-0.0668` n `25`; metal avg `-0.0851` n `20`; unknown avg `3.0247` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
