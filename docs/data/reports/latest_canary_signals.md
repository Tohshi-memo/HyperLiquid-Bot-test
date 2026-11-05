# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T20:52:29.547528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0676` n `13`; crypto_alt avg `0.1359` n `239`; crypto_major avg `0.2272` n `8`; equity avg `0.342` n `158`; fx avg `-0.0065` n `6`; index avg `0.0404` n `27`; metal avg `0.0481` n `20`; unknown avg `1.174` n `1228`
- 1h: commodity avg `0.0453` n `13`; crypto_alt avg `-0.2287` n `239`; crypto_major avg `-0.0645` n `8`; equity avg `-1.1188` n `158`; fx avg `-0.0127` n `6`; index avg `-0.1682` n `27`; metal avg `-0.1788` n `20`; unknown avg `13.0349` n `1200`
- 4h: commodity avg `0.2346` n `13`; crypto_alt avg `0.5746` n `239`; crypto_major avg `-0.6116` n `8`; equity avg `-1.403` n `158`; fx avg `-0.0071` n `6`; index avg `-0.293` n `27`; metal avg `-0.221` n `20`; unknown avg `1.8691` n `1202`
- 24h: commodity avg `0.7534` n `13`; crypto_alt avg `-3.5685` n `239`; crypto_major avg `-4.2851` n `8`; equity avg `-7.4407` n `158`; fx avg `0.0845` n `6`; index avg `-1.0727` n `27`; metal avg `0.211` n `20`; unknown avg `222.9705` n `1048`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2314`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
