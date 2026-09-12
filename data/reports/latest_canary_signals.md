# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T04:37:29.883841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.028` n `12`; crypto_alt avg `0.1293` n `233`; crypto_major avg `0.1314` n `8`; equity avg `0.0218` n `136`; fx avg `-0.0004` n `6`; index avg `-0.0028` n `26`; metal avg `0.0113` n `20`; unknown avg `-0.0213` n `832`
- 1h: commodity avg `-0.05` n `12`; crypto_alt avg `0.0953` n `233`; crypto_major avg `0.0568` n `8`; equity avg `-0.0245` n `136`; fx avg `0.0058` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.6466` n `818`
- 4h: commodity avg `-0.0978` n `12`; crypto_alt avg `0.4525` n `233`; crypto_major avg `0.1711` n `8`; equity avg `-0.051` n `136`; fx avg `0.0116` n `6`; index avg `-0.0116` n `26`; metal avg `-0.0353` n `20`; unknown avg `0.4211` n `814`
- 24h: commodity avg `-0.6767` n `12`; crypto_alt avg `0.844` n `233`; crypto_major avg `1.0456` n `8`; equity avg `0.869` n `136`; fx avg `-0.1018` n `6`; index avg `0.2482` n `26`; metal avg `0.1632` n `20`; unknown avg `2.3118` n `690`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
