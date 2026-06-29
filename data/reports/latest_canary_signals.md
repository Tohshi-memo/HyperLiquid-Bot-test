# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T00:07:26.206363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0254` n `12`; crypto_alt avg `-0.3101` n `228`; crypto_major avg `-0.5283` n `8`; equity avg `-0.298` n `88`; fx avg `0.0173` n `6`; index avg `-0.1231` n `23`; metal avg `-0.0901` n `20`; unknown avg `1.6775` n `764`
- 1h: commodity avg `-0.1136` n `12`; crypto_alt avg `0.1269` n `228`; crypto_major avg `0.0447` n `8`; equity avg `-0.2112` n `88`; fx avg `0.0197` n `6`; index avg `-0.1209` n `23`; metal avg `-0.1613` n `20`; unknown avg `1.5123` n `764`
- 4h: commodity avg `-0.5502` n `12`; crypto_alt avg `-0.2347` n `228`; crypto_major avg `-0.3086` n `8`; equity avg `-0.0174` n `88`; fx avg `-0.0383` n `6`; index avg `-0.0261` n `23`; metal avg `-0.2013` n `20`; unknown avg `-0.1659` n `762`
- 24h: commodity avg `-0.4351` n `12`; crypto_alt avg `-0.5827` n `228`; crypto_major avg `-0.9036` n `8`; equity avg `0.13` n `88`; fx avg `-0.0581` n `6`; index avg `-0.036` n `23`; metal avg `-0.2509` n `20`; unknown avg `15.7311` n `690`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
