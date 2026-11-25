# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T12:22:32.814413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1787` n `13`; crypto_alt avg `0.3175` n `239`; crypto_major avg `0.248` n `8`; equity avg `0.1798` n `168`; fx avg `0.0299` n `6`; index avg `0.022` n `27`; metal avg `0.1651` n `20`; unknown avg `15.4672` n `1263`
- 1h: commodity avg `0.1956` n `13`; crypto_alt avg `-0.114` n `239`; crypto_major avg `-0.0573` n `8`; equity avg `-0.4885` n `168`; fx avg `0.0275` n `6`; index avg `-0.0616` n `27`; metal avg `-0.0785` n `20`; unknown avg `128.5741` n `1253`
- 4h: commodity avg `0.5951` n `13`; crypto_alt avg `-0.7538` n `239`; crypto_major avg `-0.3068` n `8`; equity avg `-1.1811` n `168`; fx avg `0.0409` n `6`; index avg `-0.1789` n `27`; metal avg `-0.0916` n `20`; unknown avg `268.3743` n `1187`
- 24h: commodity avg `0.533` n `13`; crypto_alt avg `-2.1711` n `239`; crypto_major avg `-3.2109` n `8`; equity avg `-4.9659` n `168`; fx avg `0.0092` n `6`; index avg `-0.4337` n `27`; metal avg `-1.0128` n `20`; unknown avg `477.5214` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
