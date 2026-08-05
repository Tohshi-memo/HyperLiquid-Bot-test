# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T10:22:24.685169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `-0.0374` n `8`; equity avg `0.0707` n `108`; fx avg `0.0105` n `6`; index avg `0.0092` n `25`; metal avg `0.0329` n `20`; unknown avg `0.0014` n `781`
- 1h: commodity avg `0.0448` n `12`; crypto_alt avg `-0.1654` n `230`; crypto_major avg `-0.3236` n `8`; equity avg `0.1221` n `108`; fx avg `0.0321` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.0278` n `781`
- 4h: commodity avg `0.3166` n `12`; crypto_alt avg `-0.1901` n `230`; crypto_major avg `-0.1863` n `8`; equity avg `-0.7427` n `108`; fx avg `0.0559` n `6`; index avg `-0.1134` n `25`; metal avg `-0.1512` n `20`; unknown avg `0.6458` n `781`
- 24h: commodity avg `-1.174` n `12`; crypto_alt avg `0.6023` n `230`; crypto_major avg `0.7328` n `8`; equity avg `2.2858` n `108`; fx avg `0.0037` n `6`; index avg `0.6007` n `25`; metal avg `1.0968` n `20`; unknown avg `0.1121` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
