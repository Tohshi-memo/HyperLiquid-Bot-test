# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T01:52:36.161782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `13`; crypto_alt avg `-0.1358` n `239`; crypto_major avg `-0.203` n `8`; equity avg `-0.0293` n `166`; fx avg `0.019` n `6`; index avg `-0.0234` n `27`; metal avg `-0.0141` n `20`; unknown avg `0.0789` n `1263`
- 1h: commodity avg `0.0682` n `13`; crypto_alt avg `-0.2509` n `239`; crypto_major avg `-0.4575` n `8`; equity avg `-0.1363` n `166`; fx avg `0.0905` n `6`; index avg `-0.0331` n `27`; metal avg `0.0148` n `20`; unknown avg `-0.0179` n `1259`
- 4h: commodity avg `-0.2696` n `13`; crypto_alt avg `-0.4859` n `239`; crypto_major avg `-0.4611` n `8`; equity avg `0.3343` n `166`; fx avg `0.1356` n `6`; index avg `0.0463` n `27`; metal avg `0.2438` n `20`; unknown avg `13.1778` n `1216`
- 24h: commodity avg `-0.4157` n `13`; crypto_alt avg `0.1432` n `239`; crypto_major avg `0.2961` n `8`; equity avg `1.1776` n `166`; fx avg `0.1845` n `6`; index avg `0.1321` n `27`; metal avg `0.255` n `20`; unknown avg `242.4585` n `1031`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
