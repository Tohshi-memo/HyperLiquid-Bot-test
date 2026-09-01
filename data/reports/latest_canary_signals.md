# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T14:37:29.196931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.1504` n `232`; crypto_major avg `0.1326` n `8`; equity avg `0.1175` n `131`; fx avg `0.0` n `6`; index avg `0.0211` n `26`; metal avg `-0.0322` n `20`; unknown avg `-0.0003` n `792`
- 1h: commodity avg `-0.0838` n `12`; crypto_alt avg `0.7761` n `232`; crypto_major avg `0.6735` n `8`; equity avg `0.1398` n `131`; fx avg `-0.0045` n `6`; index avg `0.071` n `26`; metal avg `0.0806` n `20`; unknown avg `0.2093` n `790`
- 4h: commodity avg `-0.102` n `12`; crypto_alt avg `0.3834` n `232`; crypto_major avg `0.0138` n `8`; equity avg `-0.7267` n `130`; fx avg `-0.0114` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0644` n `20`; unknown avg `-0.3179` n `790`
- 24h: commodity avg `0.3222` n `12`; crypto_alt avg `1.7154` n `232`; crypto_major avg `0.5992` n `8`; equity avg `-1.1604` n `130`; fx avg `0.051` n `6`; index avg `-0.1758` n `26`; metal avg `-0.5094` n `20`; unknown avg `0.0895` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0401`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0337`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0323`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0312`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0301`, n `668`, weak_sample_signal
