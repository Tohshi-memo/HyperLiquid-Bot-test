# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T04:37:23.947378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `13`; crypto_alt avg `0.3846` n `239`; crypto_major avg `0.2386` n `8`; equity avg `0.2467` n `158`; fx avg `0.0098` n `6`; index avg `0.0231` n `27`; metal avg `0.0802` n `20`; unknown avg `-0.0364` n `1261`
- 1h: commodity avg `0.0703` n `13`; crypto_alt avg `0.1961` n `239`; crypto_major avg `0.1577` n `8`; equity avg `-0.2715` n `158`; fx avg `-0.0054` n `6`; index avg `-0.0464` n `27`; metal avg `0.0919` n `20`; unknown avg `19.4074` n `1247`
- 4h: commodity avg `0.254` n `13`; crypto_alt avg `0.8104` n `239`; crypto_major avg `0.282` n `8`; equity avg `1.3592` n `158`; fx avg `-0.0337` n `6`; index avg `0.1991` n `27`; metal avg `0.3369` n `20`; unknown avg `1.1436` n `1232`
- 24h: commodity avg `0.1925` n `13`; crypto_alt avg `-1.4016` n `239`; crypto_major avg `-2.135` n `8`; equity avg `0.607` n `158`; fx avg `-0.0823` n `6`; index avg `0.0675` n `27`; metal avg `0.5851` n `20`; unknown avg `1.5488` n `984`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
