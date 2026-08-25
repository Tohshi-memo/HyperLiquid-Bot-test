# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T08:52:30.720432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0924` n `12`; crypto_alt avg `-0.3169` n `231`; crypto_major avg `-0.3931` n `8`; equity avg `0.0125` n `122`; fx avg `0.0083` n `6`; index avg `0.013` n `25`; metal avg `-0.0485` n `20`; unknown avg `-0.0959` n `794`
- 1h: commodity avg `-0.2653` n `12`; crypto_alt avg `0.2221` n `231`; crypto_major avg `-0.0105` n `8`; equity avg `0.2496` n `122`; fx avg `-0.0003` n `6`; index avg `0.0493` n `25`; metal avg `-0.0877` n `20`; unknown avg `-0.0559` n `794`
- 4h: commodity avg `-0.3541` n `12`; crypto_alt avg `-0.9495` n `231`; crypto_major avg `-0.7713` n `8`; equity avg `0.5535` n `122`; fx avg `0.0625` n `6`; index avg `0.1114` n `25`; metal avg `-0.0294` n `20`; unknown avg `-0.3119` n `778`
- 24h: commodity avg `-0.403` n `12`; crypto_alt avg `1.2258` n `231`; crypto_major avg `2.3288` n `8`; equity avg `0.2676` n `122`; fx avg `0.0366` n `6`; index avg `0.0462` n `25`; metal avg `-0.2403` n `20`; unknown avg `0.185` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
