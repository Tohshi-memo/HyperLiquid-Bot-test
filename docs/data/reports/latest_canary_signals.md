# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T20:22:27.168425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `-0.0399` n `229`; crypto_major avg `0.0138` n `8`; equity avg `0.009` n `92`; fx avg `0.0013` n `6`; index avg `0.0165` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0211` n `765`
- 1h: commodity avg `-0.0313` n `12`; crypto_alt avg `0.1785` n `229`; crypto_major avg `0.2382` n `8`; equity avg `-0.0705` n `92`; fx avg `-0.0047` n `6`; index avg `0.0193` n `25`; metal avg `0.0733` n `20`; unknown avg `-0.0501` n `765`
- 4h: commodity avg `0.1266` n `12`; crypto_alt avg `-0.0784` n `229`; crypto_major avg `-0.1258` n `8`; equity avg `-0.0776` n `92`; fx avg `-0.0241` n `6`; index avg `0.0258` n `25`; metal avg `0.0221` n `20`; unknown avg `-0.2382` n `765`
- 24h: commodity avg `-0.2413` n `12`; crypto_alt avg `0.5781` n `229`; crypto_major avg `0.7548` n `8`; equity avg `-0.6186` n `92`; fx avg `-0.1565` n `6`; index avg `0.0417` n `25`; metal avg `0.1619` n `20`; unknown avg `-0.1814` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
