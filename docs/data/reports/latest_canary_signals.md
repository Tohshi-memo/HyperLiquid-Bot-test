# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T18:37:24.964735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.0915` n `232`; crypto_major avg `-0.151` n `8`; equity avg `-0.0365` n `134`; fx avg `-0.0043` n `6`; index avg `0.0022` n `26`; metal avg `0.0175` n `20`; unknown avg `-0.1687` n `796`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.2397` n `232`; crypto_major avg `-0.1571` n `8`; equity avg `-0.0016` n `134`; fx avg `-0.0065` n `6`; index avg `0.003` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.0892` n `774`
- 4h: commodity avg `-0.0501` n `12`; crypto_alt avg `-0.6111` n `232`; crypto_major avg `-0.3528` n `8`; equity avg `0.1213` n `134`; fx avg `-0.0165` n `6`; index avg `0.0462` n `26`; metal avg `0.0401` n `20`; unknown avg `-0.6684` n `768`
- 24h: commodity avg `0.1766` n `12`; crypto_alt avg `-0.1377` n `232`; crypto_major avg `-1.2823` n `8`; equity avg `0.4197` n `134`; fx avg `-0.1183` n `6`; index avg `0.0794` n `26`; metal avg `0.0001` n `20`; unknown avg `1.1652` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
