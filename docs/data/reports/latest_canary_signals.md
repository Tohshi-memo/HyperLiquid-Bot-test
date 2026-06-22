# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T15:22:35.406642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0858` n `12`; crypto_alt avg `-0.0534` n `228`; crypto_major avg `0.0285` n `8`; equity avg `-0.1665` n `79`; fx avg `0.0109` n `6`; index avg `-0.0184` n `23`; metal avg `-0.0651` n `20`; unknown avg `-0.0705` n `722`
- 1h: commodity avg `-0.0561` n `12`; crypto_alt avg `-0.5016` n `228`; crypto_major avg `-0.5003` n `8`; equity avg `-0.6259` n `79`; fx avg `-0.0266` n `6`; index avg `-0.0901` n `23`; metal avg `-0.0709` n `20`; unknown avg `0.0963` n `722`
- 4h: commodity avg `-0.4431` n `12`; crypto_alt avg `0.0784` n `228`; crypto_major avg `0.1942` n `8`; equity avg `-0.49` n `79`; fx avg `-0.0372` n `6`; index avg `-0.0058` n `23`; metal avg `-0.2282` n `20`; unknown avg `0.2784` n `722`
- 24h: commodity avg `-0.7712` n `12`; crypto_alt avg `0.103` n `228`; crypto_major avg `0.3272` n `8`; equity avg `-0.44` n `79`; fx avg `-0.0392` n `6`; index avg `0.1004` n `23`; metal avg `0.2795` n `18`; unknown avg `0.7375` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
