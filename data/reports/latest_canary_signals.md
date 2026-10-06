# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T03:52:29.204104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `0.0685` n `235`; crypto_major avg `0.0964` n `8`; equity avg `-0.0012` n `149`; fx avg `0.0036` n `6`; index avg `-0.0035` n `26`; metal avg `0.0068` n `20`; unknown avg `1.7029` n `1074`
- 1h: commodity avg `0.012` n `13`; crypto_alt avg `-0.2629` n `235`; crypto_major avg `-0.1243` n `8`; equity avg `0.0631` n `149`; fx avg `0.0004` n `6`; index avg `0.0113` n `26`; metal avg `-0.0319` n `20`; unknown avg `1.1512` n `1072`
- 4h: commodity avg `0.1167` n `13`; crypto_alt avg `-1.5087` n `235`; crypto_major avg `-0.5345` n `8`; equity avg `-0.1767` n `149`; fx avg `-0.0087` n `6`; index avg `-0.0503` n `26`; metal avg `-0.0402` n `20`; unknown avg `-0.0512` n `1066`
- 24h: commodity avg `0.0223` n `13`; crypto_alt avg `-1.1396` n `235`; crypto_major avg `-0.3496` n `8`; equity avg `0.0235` n `149`; fx avg `0.0666` n `6`; index avg `0.0952` n `26`; metal avg `-0.0262` n `20`; unknown avg `598.4376` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
