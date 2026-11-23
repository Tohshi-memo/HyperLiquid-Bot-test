# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T00:37:25.875002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `13`; crypto_alt avg `0.002` n `239`; crypto_major avg `-0.0498` n `8`; equity avg `0.0464` n `166`; fx avg `0.0121` n `6`; index avg `-0.0083` n `27`; metal avg `-0.056` n `20`; unknown avg `0.0384` n `1265`
- 1h: commodity avg `-0.0044` n `13`; crypto_alt avg `0.0208` n `239`; crypto_major avg `-0.2042` n `8`; equity avg `0.1775` n `166`; fx avg `-0.0392` n `6`; index avg `0.097` n `27`; metal avg `-0.1147` n `20`; unknown avg `-0.1547` n `1253`
- 4h: commodity avg `-0.3757` n `13`; crypto_alt avg `-0.0305` n `239`; crypto_major avg `0.3743` n `8`; equity avg `0.5816` n `166`; fx avg `0.0841` n `6`; index avg `0.0979` n `27`; metal avg `0.2206` n `20`; unknown avg `4.2178` n `1200`
- 24h: commodity avg `-0.4744` n `13`; crypto_alt avg `0.5671` n `239`; crypto_major avg `0.8507` n `8`; equity avg `1.2382` n `166`; fx avg `0.068` n `6`; index avg `0.1467` n `27`; metal avg `0.2296` n `20`; unknown avg `242.3266` n `1031`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
