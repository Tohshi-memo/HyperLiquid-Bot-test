# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T14:52:32.256531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0467` n `13`; crypto_alt avg `-0.0158` n `239`; crypto_major avg `0.0283` n `8`; equity avg `0.0328` n `161`; fx avg `-0.0023` n `6`; index avg `0.0139` n `27`; metal avg `0.0208` n `20`; unknown avg `0.6964` n `1261`
- 1h: commodity avg `0.2003` n `13`; crypto_alt avg `-0.1499` n `239`; crypto_major avg `-0.1682` n `8`; equity avg `-0.3912` n `161`; fx avg `-0.0348` n `6`; index avg `-0.049` n `27`; metal avg `-0.1978` n `20`; unknown avg `19.4322` n `1237`
- 4h: commodity avg `0.2066` n `13`; crypto_alt avg `0.1422` n `239`; crypto_major avg `-0.1847` n `8`; equity avg `-0.3493` n `161`; fx avg `-0.0637` n `6`; index avg `-0.0412` n `27`; metal avg `-0.3081` n `20`; unknown avg `128.1202` n `1231`
- 24h: commodity avg `1.0669` n `13`; crypto_alt avg `-0.7881` n `239`; crypto_major avg `-0.5285` n `8`; equity avg `2.961` n `161`; fx avg `-0.2457` n `6`; index avg `0.2653` n `27`; metal avg `0.2901` n `20`; unknown avg `1.4924` n `1155`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2806`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
