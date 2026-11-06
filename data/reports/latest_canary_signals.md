# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T05:22:28.807854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0422` n `13`; crypto_alt avg `-0.0487` n `239`; crypto_major avg `-0.0982` n `8`; equity avg `-0.3721` n `158`; fx avg `0.024` n `6`; index avg `-0.0489` n `27`; metal avg `-0.1069` n `20`; unknown avg `3.0859` n `1254`
- 1h: commodity avg `-0.1988` n `13`; crypto_alt avg `-0.1322` n `239`; crypto_major avg `-0.105` n `8`; equity avg `-0.0581` n `158`; fx avg `0.0336` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0265` n `20`; unknown avg `81.8246` n `1250`
- 4h: commodity avg `0.0526` n `13`; crypto_alt avg `0.3502` n `239`; crypto_major avg `-0.4789` n `8`; equity avg `0.7681` n `158`; fx avg `0.0221` n `6`; index avg `0.1656` n `27`; metal avg `-0.2255` n `20`; unknown avg `1.7397` n `1244`
- 24h: commodity avg `1.3665` n `13`; crypto_alt avg `-4.3137` n `239`; crypto_major avg `-5.8559` n `8`; equity avg `-5.912` n `158`; fx avg `0.0561` n `6`; index avg `-0.7526` n `27`; metal avg `-0.584` n `20`; unknown avg `230.9041` n `1033`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
