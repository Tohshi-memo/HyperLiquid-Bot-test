# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T09:22:27.437466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `13`; crypto_alt avg `-0.0056` n `239`; crypto_major avg `-0.0804` n `8`; equity avg `-0.1234` n `158`; fx avg `0.0012` n `6`; index avg `-0.0153` n `27`; metal avg `-0.0043` n `20`; unknown avg `128.0193` n `1261`
- 1h: commodity avg `0.0015` n `13`; crypto_alt avg `-0.1122` n `239`; crypto_major avg `-0.1109` n `8`; equity avg `0.0636` n `158`; fx avg `0.0125` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0038` n `20`; unknown avg `132.7366` n `1215`
- 4h: commodity avg `0.0684` n `13`; crypto_alt avg `-0.1977` n `239`; crypto_major avg `0.2035` n `8`; equity avg `0.1314` n `158`; fx avg `-0.024` n `6`; index avg `0.0258` n `27`; metal avg `-0.0124` n `20`; unknown avg `137.1689` n `1177`
- 24h: commodity avg `0.1232` n `13`; crypto_alt avg `-0.5065` n `239`; crypto_major avg `-0.232` n `8`; equity avg `-0.2006` n `158`; fx avg `0.0289` n `6`; index avg `0.0154` n `27`; metal avg `-0.0742` n `20`; unknown avg `7.9647` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
