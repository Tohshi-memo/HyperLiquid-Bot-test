# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T14:37:38.542881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0299` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0827` n `12`; crypto_alt avg `-0.584` n `228`; crypto_major avg `-0.5126` n `8`; equity avg `-0.3335` n `79`; fx avg `0.0001` n `6`; index avg `-0.0412` n `23`; metal avg `-0.0519` n `20`; unknown avg `0.1654` n `722`
- 1h: commodity avg `0.0261` n `12`; crypto_alt avg `-0.8699` n `228`; crypto_major avg `-1.0745` n `8`; equity avg `-0.6695` n `79`; fx avg `-0.0216` n `6`; index avg `-0.0446` n `23`; metal avg `-0.1694` n `20`; unknown avg `0.5826` n `722`
- 4h: commodity avg `-0.3823` n `12`; crypto_alt avg `0.4211` n `228`; crypto_major avg `0.4768` n `8`; equity avg `-0.0645` n `79`; fx avg `-0.0259` n `6`; index avg `0.0797` n `23`; metal avg `-0.2254` n `20`; unknown avg `0.9794` n `722`
- 24h: commodity avg `-0.6496` n `12`; crypto_alt avg `0.0951` n `228`; crypto_major avg `0.5502` n `8`; equity avg `-0.0886` n `79`; fx avg `-0.0168` n `6`; index avg `0.1487` n `23`; metal avg `0.3226` n `18`; unknown avg `0.8319` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
