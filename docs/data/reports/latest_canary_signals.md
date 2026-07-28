# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T23:27:20.095237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0712` n `12`; crypto_alt avg `0.1723` n `230`; crypto_major avg `-0.043` n `8`; equity avg `0.4273` n `102`; fx avg `0.008` n `6`; index avg `0.0648` n `25`; metal avg `0.0134` n `20`; unknown avg `0.1019` n `776`
- 1h: commodity avg `0.2115` n `12`; crypto_alt avg `-0.5003` n `230`; crypto_major avg `-0.8023` n `8`; equity avg `-0.8152` n `102`; fx avg `-0.0098` n `6`; index avg `-0.0782` n `25`; metal avg `-0.0154` n `20`; unknown avg `0.4341` n `776`
- 4h: commodity avg `0.7142` n `12`; crypto_alt avg `-0.311` n `230`; crypto_major avg `-0.4167` n `8`; equity avg `-0.4331` n `102`; fx avg `-0.0194` n `6`; index avg `-0.1012` n `25`; metal avg `-0.0754` n `20`; unknown avg `0.357` n `776`
- 24h: commodity avg `-0.2086` n `12`; crypto_alt avg `-0.7753` n `230`; crypto_major avg `-0.682` n `8`; equity avg `-2.9829` n `102`; fx avg `-0.0936` n `6`; index avg `-0.4112` n `25`; metal avg `-0.4446` n `20`; unknown avg `0.252` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
