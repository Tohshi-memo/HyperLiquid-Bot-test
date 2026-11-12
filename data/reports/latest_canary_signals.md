# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T07:22:29.961648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `13`; crypto_alt avg `0.1085` n `239`; crypto_major avg `0.1214` n `8`; equity avg `-0.1083` n `161`; fx avg `0.0121` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0253` n `20`; unknown avg `0.0683` n `1262`
- 1h: commodity avg `0.1199` n `13`; crypto_alt avg `-0.0526` n `239`; crypto_major avg `-0.1283` n `8`; equity avg `-0.109` n `161`; fx avg `0.0653` n `6`; index avg `-0.0512` n `27`; metal avg `-0.1172` n `20`; unknown avg `0.3837` n `1252`
- 4h: commodity avg `0.2782` n `13`; crypto_alt avg `-0.2573` n `239`; crypto_major avg `-0.3842` n `8`; equity avg `-0.8813` n `161`; fx avg `0.0431` n `6`; index avg `-0.123` n `27`; metal avg `-0.0889` n `20`; unknown avg `0.1646` n `1204`
- 24h: commodity avg `0.3952` n `13`; crypto_alt avg `-1.3559` n `239`; crypto_major avg `-0.7015` n `8`; equity avg `-0.5109` n `161`; fx avg `-0.1424` n `6`; index avg `-0.0898` n `27`; metal avg `-0.711` n `20`; unknown avg `-0.2465` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
