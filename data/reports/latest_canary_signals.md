# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T13:22:30.831307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `13`; crypto_alt avg `-0.5113` n `239`; crypto_major avg `-0.499` n `8`; equity avg `-0.3633` n `166`; fx avg `-0.0025` n `6`; index avg `-0.0515` n `27`; metal avg `-0.0084` n `20`; unknown avg `0.4346` n `1267`
- 1h: commodity avg `0.0441` n `13`; crypto_alt avg `-0.9125` n `239`; crypto_major avg `-0.6252` n `8`; equity avg `-0.2427` n `166`; fx avg `0.0368` n `6`; index avg `-0.0339` n `27`; metal avg `0.0703` n `20`; unknown avg `158.6135` n `1261`
- 4h: commodity avg `0.1143` n `13`; crypto_alt avg `-1.4399` n `239`; crypto_major avg `-0.3288` n `8`; equity avg `-1.0309` n `166`; fx avg `0.1271` n `6`; index avg `-0.1756` n `27`; metal avg `0.1714` n `20`; unknown avg `446.6452` n `1218`
- 24h: commodity avg `-0.3019` n `13`; crypto_alt avg `-2.1622` n `239`; crypto_major avg `-1.7951` n `8`; equity avg `0.9447` n `166`; fx avg `0.0271` n `6`; index avg `0.2174` n `27`; metal avg `-0.2412` n `20`; unknown avg `335.8112` n `1142`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
