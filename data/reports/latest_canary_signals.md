# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T23:22:17.299158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.378` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0792` n `12`; crypto_alt avg `-0.1975` n `228`; crypto_major avg `-0.1235` n `8`; equity avg `-0.0051` n `67`; fx avg `-0.011` n `6`; index avg `-0.012` n `23`; metal avg `-0.0669` n `18`; unknown avg `4.4006` n `419`
- 1h: commodity avg `0.1787` n `12`; crypto_alt avg `-0.5133` n `228`; crypto_major avg `-0.5685` n `8`; equity avg `-0.0171` n `67`; fx avg `-0.0124` n `6`; index avg `-0.0585` n `23`; metal avg `-0.2037` n `18`; unknown avg `0.6346` n `419`
- 4h: commodity avg `0.2411` n `12`; crypto_alt avg `-2.1647` n `228`; crypto_major avg `-1.3885` n `8`; equity avg `0.0019` n `67`; fx avg `-0.0213` n `6`; index avg `-0.0105` n `23`; metal avg `-0.0321` n `18`; unknown avg `0.2133` n `419`
- 24h: commodity avg `-0.9812` n `12`; crypto_alt avg `-2.458` n `228`; crypto_major avg `-1.544` n `8`; equity avg `-0.2484` n `67`; fx avg `-0.1044` n `6`; index avg `-0.5394` n `23`; metal avg `-1.4364` n `18`; unknown avg `-0.4015` n `400`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
