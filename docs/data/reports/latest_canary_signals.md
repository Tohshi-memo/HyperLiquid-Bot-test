# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T06:07:29.059199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `13`; crypto_alt avg `0.0386` n `239`; crypto_major avg `0.0622` n `8`; equity avg `0.0995` n `158`; fx avg `0.0063` n `6`; index avg `0.0253` n `27`; metal avg `0.0759` n `20`; unknown avg `-0.182` n `1243`
- 1h: commodity avg `0.1447` n `13`; crypto_alt avg `-0.2068` n `239`; crypto_major avg `-0.1283` n `8`; equity avg `-0.3348` n `158`; fx avg `0.0102` n `6`; index avg `-0.0442` n `27`; metal avg `-0.1217` n `20`; unknown avg `-0.1214` n `1237`
- 4h: commodity avg `0.1245` n `13`; crypto_alt avg `-0.5322` n `239`; crypto_major avg `-0.6249` n `8`; equity avg `-0.9653` n `158`; fx avg `0.0133` n `6`; index avg `-0.1946` n `27`; metal avg `-0.1929` n `20`; unknown avg `0.0319` n `1215`
- 24h: commodity avg `-1.9575` n `13`; crypto_alt avg `1.1574` n `239`; crypto_major avg `2.1602` n `8`; equity avg `-2.6584` n `158`; fx avg `0.0961` n `6`; index avg `-0.1252` n `27`; metal avg `0.9029` n `20`; unknown avg `30.5262` n `1012`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2524`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
