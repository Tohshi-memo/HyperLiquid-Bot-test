# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T04:52:26.741542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.1185` n `228`; crypto_major avg `0.1513` n `8`; equity avg `0.0279` n `88`; fx avg `0.0022` n `6`; index avg `0.0014` n `23`; metal avg `-0.0187` n `20`; unknown avg `0.1854` n `764`
- 1h: commodity avg `-0.0148` n `12`; crypto_alt avg `0.249` n `228`; crypto_major avg `-0.0137` n `8`; equity avg `-0.0077` n `88`; fx avg `0.0083` n `6`; index avg `0.0113` n `23`; metal avg `-0.0168` n `20`; unknown avg `-0.3468` n `756`
- 4h: commodity avg `-0.1259` n `12`; crypto_alt avg `0.4341` n `228`; crypto_major avg `0.0396` n `8`; equity avg `-0.0384` n `88`; fx avg `-0.0047` n `6`; index avg `-0.0069` n `23`; metal avg `0.0164` n `20`; unknown avg `15.5773` n `714`
- 24h: commodity avg `0.2331` n `12`; crypto_alt avg `-0.3084` n `228`; crypto_major avg `-1.2403` n `8`; equity avg `0.0321` n `88`; fx avg `-0.0065` n `6`; index avg `-0.1072` n `23`; metal avg `-0.0403` n `20`; unknown avg `16.3274` n `666`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
