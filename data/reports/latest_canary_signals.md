# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T03:07:28.959536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.1304` n `232`; crypto_major avg `-0.1149` n `8`; equity avg `0.0224` n `133`; fx avg `-0.0064` n `6`; index avg `0.0105` n `26`; metal avg `0.0606` n `20`; unknown avg `-0.0135` n `790`
- 1h: commodity avg `-0.0712` n `12`; crypto_alt avg `0.5519` n `232`; crypto_major avg `0.685` n `8`; equity avg `0.1418` n `133`; fx avg `-0.0332` n `6`; index avg `0.0284` n `26`; metal avg `0.0592` n `20`; unknown avg `0.8503` n `790`
- 4h: commodity avg `0.0555` n `12`; crypto_alt avg `1.026` n `232`; crypto_major avg `1.0069` n `8`; equity avg `0.1388` n `133`; fx avg `-0.0913` n `6`; index avg `-0.0158` n `26`; metal avg `0.1954` n `20`; unknown avg `0.5802` n `790`
- 24h: commodity avg `0.1573` n `12`; crypto_alt avg `0.3534` n `232`; crypto_major avg `0.5544` n `8`; equity avg `1.427` n `133`; fx avg `-0.3921` n `6`; index avg `0.1554` n `26`; metal avg `0.8781` n `20`; unknown avg `-0.0354` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
