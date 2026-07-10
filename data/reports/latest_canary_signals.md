# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T17:07:34.743863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.021` n `229`; crypto_major avg `0.0055` n `8`; equity avg `-0.1251` n `92`; fx avg `0.0057` n `6`; index avg `-0.0323` n `25`; metal avg `-0.0394` n `20`; unknown avg `0.0062` n `765`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `0.1986` n `229`; crypto_major avg `0.1645` n `8`; equity avg `0.2265` n `92`; fx avg `0.0132` n `6`; index avg `0.0186` n `25`; metal avg `-0.0826` n `20`; unknown avg `0.011` n `765`
- 4h: commodity avg `-0.2243` n `12`; crypto_alt avg `-0.0666` n `229`; crypto_major avg `-0.2209` n `8`; equity avg `-0.2361` n `92`; fx avg `-0.0517` n `6`; index avg `0.1068` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.1647` n `765`
- 24h: commodity avg `-0.3936` n `12`; crypto_alt avg `1.1971` n `229`; crypto_major avg `1.3364` n `8`; equity avg `-0.7102` n `92`; fx avg `-0.1537` n `6`; index avg `0.0225` n `25`; metal avg `-0.1593` n `20`; unknown avg `-0.1732` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
