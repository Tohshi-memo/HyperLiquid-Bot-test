# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T09:22:29.253057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0146` n `13`; crypto_alt avg `-0.061` n `239`; crypto_major avg `-0.0355` n `8`; equity avg `0.0598` n `158`; fx avg `-0.0174` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0196` n `20`; unknown avg `0.1471` n `1265`
- 1h: commodity avg `0.0464` n `13`; crypto_alt avg `0.1247` n `239`; crypto_major avg `-0.0867` n `8`; equity avg `-0.209` n `158`; fx avg `0.0118` n `6`; index avg `-0.0632` n `27`; metal avg `0.0173` n `20`; unknown avg `1.1897` n `1205`
- 4h: commodity avg `0.3789` n `13`; crypto_alt avg `0.4122` n `239`; crypto_major avg `0.1833` n `8`; equity avg `0.1851` n `158`; fx avg `-0.0252` n `6`; index avg `0.0134` n `27`; metal avg `-0.0489` n `20`; unknown avg `0.7643` n `1161`
- 24h: commodity avg `-1.5759` n `13`; crypto_alt avg `1.0076` n `239`; crypto_major avg `1.8802` n `8`; equity avg `-2.6603` n `158`; fx avg `-0.0293` n `6`; index avg `-0.2272` n `27`; metal avg `0.6223` n `20`; unknown avg `0.7265` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2463`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
