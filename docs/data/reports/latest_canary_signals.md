# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T12:07:27.317146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0688` n `12`; crypto_alt avg `-0.0875` n `230`; crypto_major avg `-0.1613` n `8`; equity avg `-0.1712` n `92`; fx avg `-0.005` n `6`; index avg `-0.0359` n `25`; metal avg `-0.0723` n `20`; unknown avg `0.0044` n `766`
- 1h: commodity avg `-0.1396` n `12`; crypto_alt avg `0.0103` n `230`; crypto_major avg `-0.053` n `8`; equity avg `-0.0472` n `92`; fx avg `0.0092` n `6`; index avg `0.0413` n `25`; metal avg `-0.004` n `20`; unknown avg `0.013` n `766`
- 4h: commodity avg `-0.129` n `12`; crypto_alt avg `0.0351` n `230`; crypto_major avg `0.3183` n `8`; equity avg `-0.1586` n `92`; fx avg `0.0422` n `6`; index avg `0.0612` n `25`; metal avg `-0.0992` n `20`; unknown avg `0.0621` n `766`
- 24h: commodity avg `1.1883` n `12`; crypto_alt avg `-0.8522` n `230`; crypto_major avg `-0.3664` n `8`; equity avg `-0.7834` n `92`; fx avg `-0.0083` n `6`; index avg `-0.0335` n `25`; metal avg `-0.1669` n `20`; unknown avg `-0.3012` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
