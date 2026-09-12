# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T14:37:30.843184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.0187` n `233`; crypto_major avg `0.0021` n `8`; equity avg `-0.0119` n `136`; fx avg `0.0045` n `6`; index avg `0.0042` n `26`; metal avg `0.0037` n `20`; unknown avg `3.1875` n `838`
- 1h: commodity avg `-0.0307` n `12`; crypto_alt avg `0.1759` n `233`; crypto_major avg `0.1208` n `8`; equity avg `0.0065` n `136`; fx avg `0.0019` n `6`; index avg `0.0043` n `26`; metal avg `0.0094` n `20`; unknown avg `0.8257` n `836`
- 4h: commodity avg `-0.0164` n `12`; crypto_alt avg `0.0962` n `233`; crypto_major avg `0.1667` n `8`; equity avg `0.0116` n `136`; fx avg `-0.0001` n `6`; index avg `0.0019` n `26`; metal avg `0.0345` n `20`; unknown avg `1.1387` n `824`
- 24h: commodity avg `-0.2654` n `12`; crypto_alt avg `-0.3486` n `233`; crypto_major avg `-1.3386` n `8`; equity avg `-0.2775` n `136`; fx avg `-0.0186` n `6`; index avg `0.0436` n `26`; metal avg `-0.1077` n `20`; unknown avg `10.4525` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
