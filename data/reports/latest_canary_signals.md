# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T21:22:28.015299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `13`; crypto_alt avg `0.0395` n `235`; crypto_major avg `0.0525` n `8`; equity avg `0.0196` n `143`; fx avg `-0.0051` n `6`; index avg `0.002` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.048` n `1079`
- 1h: commodity avg `0.1143` n `13`; crypto_alt avg `-0.01` n `235`; crypto_major avg `-0.1311` n `8`; equity avg `-0.0091` n `143`; fx avg `-0.0015` n `6`; index avg `-0.0047` n `26`; metal avg `0.0016` n `20`; unknown avg `-0.2635` n `1077`
- 4h: commodity avg `0.0327` n `13`; crypto_alt avg `-0.0434` n `235`; crypto_major avg `-0.1723` n `8`; equity avg `0.0621` n `143`; fx avg `0.0005` n `6`; index avg `0.0062` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.0223` n `1062`
- 24h: commodity avg `0.0537` n `13`; crypto_alt avg `2.7465` n `235`; crypto_major avg `1.3346` n `8`; equity avg `0.1769` n `143`; fx avg `-0.0871` n `6`; index avg `0.0412` n `26`; metal avg `-0.0088` n `20`; unknown avg `-0.4643` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
