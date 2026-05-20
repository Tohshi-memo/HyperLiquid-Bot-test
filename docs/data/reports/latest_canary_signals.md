# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T02:36:16.076760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2589` n `12`; crypto_alt avg `-0.1093` n `228`; crypto_major avg `-0.1953` n `8`; equity avg `-0.4858` n `66`; fx avg `0.0457` n `6`; index avg `-0.3112` n `23`; metal avg `-0.4953` n `18`; unknown avg `-0.1052` n `384`
- 1h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.4593` n `228`; crypto_major avg `0.244` n `8`; equity avg `0.025` n `66`; fx avg `-0.0337` n `6`; index avg `-0.0115` n `23`; metal avg `0.0014` n `18`; unknown avg `-0.2238` n `384`
- 4h: commodity avg `-0.0748` n `12`; crypto_alt avg `0.3497` n `228`; crypto_major avg `-0.1751` n `8`; equity avg `-0.2663` n `66`; fx avg `-0.0309` n `6`; index avg `-0.3189` n `23`; metal avg `-0.4815` n `18`; unknown avg `-0.7243` n `383`
- 24h: commodity avg `0.7764` n `12`; crypto_alt avg `-0.6696` n `228`; crypto_major avg `-0.7344` n `8`; equity avg `0.1202` n `66`; fx avg `-0.1095` n `6`; index avg `-0.5598` n `23`; metal avg `-2.3529` n `18`; unknown avg `0.8333` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
