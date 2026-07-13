# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T17:37:26.348290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1124` n `12`; crypto_alt avg `-0.4004` n `230`; crypto_major avg `-0.3692` n `8`; equity avg `-0.2122` n `92`; fx avg `-0.0125` n `6`; index avg `-0.0272` n `25`; metal avg `-0.0508` n `20`; unknown avg `-0.1022` n `766`
- 1h: commodity avg `0.2986` n `12`; crypto_alt avg `-0.3623` n `230`; crypto_major avg `-0.1068` n `8`; equity avg `-0.0143` n `92`; fx avg `0.0036` n `6`; index avg `0.0391` n `25`; metal avg `0.0131` n `20`; unknown avg `-0.1568` n `766`
- 4h: commodity avg `0.6883` n `12`; crypto_alt avg `-0.85` n `230`; crypto_major avg `-0.6697` n `8`; equity avg `-0.9283` n `92`; fx avg `-0.0185` n `6`; index avg `-0.1163` n `25`; metal avg `-0.368` n `20`; unknown avg `-0.0429` n `766`
- 24h: commodity avg `0.4181` n `12`; crypto_alt avg `-2.409` n `230`; crypto_major avg `-3.1693` n `8`; equity avg `-3.1854` n `92`; fx avg `-0.0883` n `6`; index avg `-0.5976` n `25`; metal avg `-0.5597` n `20`; unknown avg `-0.1967` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
