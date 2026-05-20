# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T19:07:21.919439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0673` n `12`; crypto_alt avg `-0.1041` n `228`; crypto_major avg `-0.0144` n `8`; equity avg `-0.0279` n `66`; fx avg `0.0095` n `6`; index avg `0.0298` n `23`; metal avg `0.0245` n `18`; unknown avg `-0.0564` n `384`
- 1h: commodity avg `0.2281` n `12`; crypto_alt avg `-0.4479` n `228`; crypto_major avg `-0.4253` n `8`; equity avg `-0.2296` n `66`; fx avg `0.0328` n `6`; index avg `0.0989` n `23`; metal avg `-0.1047` n `18`; unknown avg `0.1164` n `384`
- 4h: commodity avg `-0.7458` n `12`; crypto_alt avg `0.4426` n `228`; crypto_major avg `0.0349` n `8`; equity avg `0.3352` n `66`; fx avg `0.0495` n `6`; index avg `0.193` n `23`; metal avg `0.4091` n `18`; unknown avg `0.7176` n `384`
- 24h: commodity avg `-2.6209` n `12`; crypto_alt avg `2.2408` n `228`; crypto_major avg `1.3747` n `8`; equity avg `1.3357` n `66`; fx avg `-0.0124` n `6`; index avg `0.9131` n `23`; metal avg `1.5165` n `18`; unknown avg `0.9342` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
