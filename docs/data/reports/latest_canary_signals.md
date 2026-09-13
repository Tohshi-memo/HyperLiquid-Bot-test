# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T15:52:32.642614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.1028` n `233`; crypto_major avg `-0.0155` n `8`; equity avg `-0.0176` n `136`; fx avg `-0.0037` n `6`; index avg `-0.0126` n `27`; metal avg `-0.0184` n `20`; unknown avg `-0.257` n `838`
- 1h: commodity avg `0.1044` n `12`; crypto_alt avg `-0.5594` n `233`; crypto_major avg `-0.2116` n `8`; equity avg `-0.1402` n `136`; fx avg `0.0044` n `6`; index avg `-0.04` n `27`; metal avg `-0.0257` n `20`; unknown avg `22.6947` n `836`
- 4h: commodity avg `0.039` n `12`; crypto_alt avg `0.1977` n `233`; crypto_major avg `0.2903` n `8`; equity avg `0.0245` n `136`; fx avg `0.0031` n `6`; index avg `-0.0058` n `27`; metal avg `-0.0147` n `20`; unknown avg `2.5304` n `826`
- 24h: commodity avg `0.3186` n `12`; crypto_alt avg `-0.6525` n `233`; crypto_major avg `-1.5445` n `8`; equity avg `-1.732` n `136`; fx avg `0.0115` n `6`; index avg `-0.3048` n `26`; metal avg `-0.1061` n `20`; unknown avg `1.8941` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
