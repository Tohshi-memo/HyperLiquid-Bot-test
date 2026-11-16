# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T02:22:22.045152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `13`; crypto_alt avg `0.5959` n `239`; crypto_major avg `0.4049` n `8`; equity avg `0.1804` n `162`; fx avg `0.0035` n `6`; index avg `0.0127` n `27`; metal avg `0.0139` n `20`; unknown avg `-0.0043` n `1261`
- 1h: commodity avg `-0.049` n `13`; crypto_alt avg `0.9715` n `239`; crypto_major avg `0.8315` n `8`; equity avg `0.3716` n `162`; fx avg `-0.0143` n `6`; index avg `0.0406` n `27`; metal avg `-0.0108` n `20`; unknown avg `0.2157` n `1259`
- 4h: commodity avg `-0.262` n `13`; crypto_alt avg `0.0634` n `239`; crypto_major avg `-0.1318` n `8`; equity avg `-0.0072` n `162`; fx avg `-0.0197` n `6`; index avg `0.0135` n `27`; metal avg `0.0224` n `20`; unknown avg `-0.0048` n `1209`
- 24h: commodity avg `-0.3927` n `13`; crypto_alt avg `0.7806` n `239`; crypto_major avg `1.5194` n `8`; equity avg `0.8924` n `162`; fx avg `-0.003` n `6`; index avg `0.1042` n `27`; metal avg `0.295` n `20`; unknown avg `1.2762` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
