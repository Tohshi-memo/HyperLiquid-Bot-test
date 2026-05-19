# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T15:22:19.631495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0686` n `12`; crypto_alt avg `-0.2405` n `228`; crypto_major avg `-0.0273` n `8`; equity avg `0.2394` n `66`; fx avg `-0.0083` n `6`; index avg `0.177` n `23`; metal avg `0.221` n `18`; unknown avg `-0.0249` n `383`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.433` n `228`; crypto_major avg `0.0467` n `8`; equity avg `0.7877` n `66`; fx avg `-0.0012` n `6`; index avg `0.3539` n `23`; metal avg `0.061` n `18`; unknown avg `-0.1143` n `383`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.6666` n `228`; crypto_major avg `-0.3646` n `8`; equity avg `-0.2826` n `66`; fx avg `-0.0248` n `6`; index avg `-0.5334` n `23`; metal avg `-1.4217` n `18`; unknown avg `-0.2631` n `383`
- 24h: commodity avg `0.6508` n `12`; crypto_alt avg `0.6382` n `228`; crypto_major avg `1.1263` n `8`; equity avg `-0.5419` n `66`; fx avg `0.2035` n `6`; index avg `-0.8858` n `23`; metal avg `-1.7817` n `18`; unknown avg `-0.0083` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
