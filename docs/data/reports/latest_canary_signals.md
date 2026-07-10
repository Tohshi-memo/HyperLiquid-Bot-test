# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T10:22:26.420374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `0.03` n `229`; crypto_major avg `0.0189` n `8`; equity avg `-0.0193` n `91`; fx avg `0.0099` n `6`; index avg `-0.006` n `25`; metal avg `0.0091` n `20`; unknown avg `0.0236` n `766`
- 1h: commodity avg `0.076` n `12`; crypto_alt avg `0.2456` n `229`; crypto_major avg `0.1283` n `8`; equity avg `0.2496` n `91`; fx avg `-0.0016` n `6`; index avg `0.0136` n `25`; metal avg `0.0411` n `20`; unknown avg `0.0406` n `766`
- 4h: commodity avg `-0.0491` n `12`; crypto_alt avg `0.4541` n `229`; crypto_major avg `0.5891` n `8`; equity avg `0.1307` n `91`; fx avg `0.0375` n `6`; index avg `0.05` n `25`; metal avg `-0.1671` n `20`; unknown avg `1.1478` n `765`
- 24h: commodity avg `-0.9773` n `12`; crypto_alt avg `1.129` n `229`; crypto_major avg `1.6208` n `8`; equity avg `0.448` n `91`; fx avg `-0.1191` n `6`; index avg `0.2399` n `25`; metal avg `0.1874` n `20`; unknown avg `0.1028` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
