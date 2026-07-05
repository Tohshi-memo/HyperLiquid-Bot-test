# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T13:52:29.847800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `0.1501` n `229`; crypto_major avg `0.1627` n `8`; equity avg `-0.0128` n `88`; fx avg `-0.0036` n `6`; index avg `0.0181` n `25`; metal avg `0.0055` n `20`; unknown avg `0.0333` n `765`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.0864` n `229`; crypto_major avg `0.0687` n `8`; equity avg `-0.0029` n `88`; fx avg `-0.0047` n `6`; index avg `0.0307` n `25`; metal avg `0.0074` n `20`; unknown avg `0.0112` n `765`
- 4h: commodity avg `-0.011` n `12`; crypto_alt avg `0.7862` n `229`; crypto_major avg `0.9651` n `8`; equity avg `0.1541` n `88`; fx avg `-0.0398` n `6`; index avg `0.0478` n `25`; metal avg `0.038` n `20`; unknown avg `0.0945` n `765`
- 24h: commodity avg `0.0059` n `12`; crypto_alt avg `-0.723` n `229`; crypto_major avg `-0.1905` n `8`; equity avg `0.3588` n `88`; fx avg `-0.0189` n `6`; index avg `0.0759` n `25`; metal avg `0.0986` n `20`; unknown avg `-1.1302` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
