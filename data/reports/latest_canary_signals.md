# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T09:07:36.058636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0847` n `13`; crypto_alt avg `-0.0015` n `239`; crypto_major avg `0.0014` n `8`; equity avg `0.3512` n `166`; fx avg `-0.0223` n `6`; index avg `0.0281` n `27`; metal avg `0.033` n `20`; unknown avg `200.6133` n `1246`
- 1h: commodity avg `-0.0464` n `13`; crypto_alt avg `-0.0313` n `239`; crypto_major avg `0.1614` n `8`; equity avg `0.5043` n `166`; fx avg `-0.0169` n `6`; index avg `0.0458` n `27`; metal avg `0.1228` n `20`; unknown avg `507.4182` n `1112`
- 4h: commodity avg `-0.3175` n `13`; crypto_alt avg `0.799` n `239`; crypto_major avg `0.7493` n `8`; equity avg `1.4428` n `166`; fx avg `-0.0103` n `6`; index avg `0.0954` n `27`; metal avg `0.1755` n `20`; unknown avg `515.8704` n `1094`
- 24h: commodity avg `-0.6241` n `13`; crypto_alt avg `1.7815` n `239`; crypto_major avg `2.3943` n `8`; equity avg `2.8225` n `166`; fx avg `0.2286` n `6`; index avg `0.1924` n `27`; metal avg `0.4737` n `20`; unknown avg `0.585` n `955`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
