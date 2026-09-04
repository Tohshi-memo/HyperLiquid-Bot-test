# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T08:22:27.741518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `0.1136` n `232`; crypto_major avg `0.1222` n `8`; equity avg `0.0297` n `133`; fx avg `-0.0065` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.0828` n `793`
- 1h: commodity avg `-0.1398` n `12`; crypto_alt avg `0.2028` n `232`; crypto_major avg `-0.0664` n `8`; equity avg `0.2512` n `133`; fx avg `0.0071` n `6`; index avg `0.0217` n `26`; metal avg `0.1388` n `20`; unknown avg `0.0522` n `791`
- 4h: commodity avg `-0.1818` n `12`; crypto_alt avg `-0.2675` n `232`; crypto_major avg `-0.4719` n `8`; equity avg `0.2113` n `133`; fx avg `-0.0362` n `6`; index avg `0.0296` n `26`; metal avg `0.1576` n `20`; unknown avg `19.4211` n `755`
- 24h: commodity avg `-0.1462` n `12`; crypto_alt avg `2.0507` n `232`; crypto_major avg `3.6661` n `8`; equity avg `1.8349` n `133`; fx avg `-0.0448` n `6`; index avg `0.3224` n `26`; metal avg `0.5178` n `20`; unknown avg `1.751` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
