# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T22:22:37.914745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `0.2641` n `239`; crypto_major avg `0.2479` n `8`; equity avg `0.1536` n `166`; fx avg `-0.0193` n `6`; index avg `0.0135` n `27`; metal avg `-0.0083` n `20`; unknown avg `0.0204` n `1260`
- 1h: commodity avg `-0.0033` n `13`; crypto_alt avg `1.437` n `239`; crypto_major avg `1.2911` n `8`; equity avg `0.2756` n `166`; fx avg `-0.0111` n `6`; index avg `0.0366` n `27`; metal avg `0.1133` n `20`; unknown avg `161.5806` n `1252`
- 4h: commodity avg `0.492` n `13`; crypto_alt avg `0.3348` n `239`; crypto_major avg `-0.1479` n `8`; equity avg `-0.6426` n `166`; fx avg `-0.0478` n `6`; index avg `-0.1387` n `27`; metal avg `0.0106` n `20`; unknown avg `166.6842` n `1216`
- 24h: commodity avg `0.2765` n `13`; crypto_alt avg `-4.4315` n `239`; crypto_major avg `-5.1117` n `8`; equity avg `-6.5772` n `166`; fx avg `0.0054` n `6`; index avg `-0.7238` n `27`; metal avg `-0.8292` n `20`; unknown avg `33.4354` n `1139`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
