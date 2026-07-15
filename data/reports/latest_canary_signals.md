# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T11:00:56.677132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `0.0006` n `230`; crypto_major avg `0.085` n `8`; equity avg `0.086` n `93`; fx avg `0.0051` n `6`; index avg `0.0182` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.0094` n `767`
- 1h: commodity avg `-0.0925` n `12`; crypto_alt avg `-0.1002` n `230`; crypto_major avg `-0.0749` n `8`; equity avg `0.0052` n `93`; fx avg `-0.0178` n `6`; index avg `0.0016` n `25`; metal avg `-0.0736` n `20`; unknown avg `-0.0676` n `767`
- 4h: commodity avg `-0.0635` n `12`; crypto_alt avg `-0.0215` n `230`; crypto_major avg `0.056` n `8`; equity avg `-0.2424` n `93`; fx avg `-0.012` n `6`; index avg `-0.065` n `25`; metal avg `-0.1579` n `20`; unknown avg `-0.1198` n `765`
- 24h: commodity avg `-0.1764` n `12`; crypto_alt avg `1.6763` n `230`; crypto_major avg `3.0556` n `8`; equity avg `1.5176` n `92`; fx avg `0.009` n `6`; index avg `0.4109` n `25`; metal avg `0.2651` n `20`; unknown avg `0.245` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
