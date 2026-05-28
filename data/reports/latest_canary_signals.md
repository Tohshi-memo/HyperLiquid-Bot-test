# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T12:37:21.587991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3496` n `12`; crypto_alt avg `0.3079` n `228`; crypto_major avg `0.2158` n `8`; equity avg `0.3723` n `67`; fx avg `0.0183` n `6`; index avg `0.1759` n `23`; metal avg `0.4506` n `18`; unknown avg `-0.0305` n `419`
- 1h: commodity avg `-0.3717` n `12`; crypto_alt avg `-0.0141` n `228`; crypto_major avg `-0.0554` n `8`; equity avg `0.4048` n `67`; fx avg `0.048` n `6`; index avg `0.2328` n `23`; metal avg `0.2372` n `18`; unknown avg `-0.0078` n `419`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `-0.5349` n `228`; crypto_major avg `-0.1265` n `8`; equity avg `0.1499` n `67`; fx avg `0.0472` n `6`; index avg `0.0696` n `23`; metal avg `-0.0839` n `18`; unknown avg `-0.2959` n `419`
- 24h: commodity avg `1.131` n `12`; crypto_alt avg `-5.7819` n `228`; crypto_major avg `-4.1154` n `8`; equity avg `-1.5008` n `67`; fx avg `-0.0585` n `6`; index avg `-1.0828` n `23`; metal avg `-1.2427` n `18`; unknown avg `-1.8357` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
