# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T12:52:26.526782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.0498` n `233`; crypto_major avg `-0.0016` n `8`; equity avg `-0.0063` n `136`; fx avg `0.0016` n `6`; index avg `0.0022` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.0295` n `838`
- 1h: commodity avg `0.0419` n `12`; crypto_alt avg `0.1172` n `233`; crypto_major avg `-0.1387` n `8`; equity avg `-0.1509` n `136`; fx avg `-0.0027` n `6`; index avg `-0.0253` n `27`; metal avg `-0.0014` n `20`; unknown avg `-0.0538` n `826`
- 4h: commodity avg `0.187` n `12`; crypto_alt avg `-0.2991` n `233`; crypto_major avg `-0.8146` n `8`; equity avg `-0.7689` n `136`; fx avg `0.0105` n `6`; index avg `-0.1416` n `27`; metal avg `-0.05` n `20`; unknown avg `0.4113` n `826`
- 24h: commodity avg `0.2894` n `12`; crypto_alt avg `-0.4685` n `233`; crypto_major avg `-1.951` n `8`; equity avg `-1.9182` n `136`; fx avg `0.0045` n `6`; index avg `-0.3112` n `26`; metal avg `-0.0839` n `20`; unknown avg `-0.0641` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
