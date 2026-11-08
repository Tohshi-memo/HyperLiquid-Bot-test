# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T10:07:26.395494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `13`; crypto_alt avg `0.0108` n `239`; crypto_major avg `-0.036` n `8`; equity avg `0.0271` n `158`; fx avg `0.0019` n `6`; index avg `0.0071` n `27`; metal avg `-0.0082` n `20`; unknown avg `5.1402` n `1258`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `-0.0346` n `239`; crypto_major avg `-0.1327` n `8`; equity avg `0.1614` n `158`; fx avg `-0.0038` n `6`; index avg `0.0032` n `27`; metal avg `-0.0101` n `20`; unknown avg `218.4514` n `1176`
- 4h: commodity avg `0.0714` n `13`; crypto_alt avg `-0.1689` n `239`; crypto_major avg `-0.0844` n `8`; equity avg `0.2116` n `158`; fx avg `-0.0044` n `6`; index avg `-0.0001` n `27`; metal avg `0.0052` n `20`; unknown avg `221.8542` n `1156`
- 24h: commodity avg `0.096` n `13`; crypto_alt avg `-1.4565` n `239`; crypto_major avg `-0.6869` n `8`; equity avg `0.1716` n `158`; fx avg `0.0495` n `6`; index avg `0.0316` n `27`; metal avg `-0.0354` n `20`; unknown avg `5.5963` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
