# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T12:37:30.673555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0238` n `12`; crypto_alt avg `0.0643` n `233`; crypto_major avg `-0.133` n `8`; equity avg `-0.0655` n `136`; fx avg `0.0005` n `6`; index avg `-0.0126` n `27`; metal avg `0.0009` n `20`; unknown avg `0.032` n `832`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `0.2244` n `233`; crypto_major avg `-0.0729` n `8`; equity avg `-0.1289` n `136`; fx avg `-0.0007` n `6`; index avg `-0.0409` n `27`; metal avg `-0.0039` n `20`; unknown avg `-0.0873` n `826`
- 4h: commodity avg `0.186` n `12`; crypto_alt avg `-0.2509` n `233`; crypto_major avg `-0.813` n `8`; equity avg `-0.7626` n `136`; fx avg `0.0089` n `6`; index avg `-0.1437` n `27`; metal avg `-0.0479` n `20`; unknown avg `0.3455` n `826`
- 24h: commodity avg `0.289` n `12`; crypto_alt avg `-0.5523` n `233`; crypto_major avg `-2.0403` n `8`; equity avg `-1.9116` n `136`; fx avg `0.0062` n `6`; index avg `-0.3127` n `26`; metal avg `-0.0773` n `20`; unknown avg `-0.1378` n `704`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
