# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T02:22:22.338256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `13`; crypto_alt avg `-0.1258` n `239`; crypto_major avg `-0.0174` n `8`; equity avg `-0.0872` n `158`; fx avg `-0.0007` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0092` n `20`; unknown avg `-0.1197` n `1261`
- 1h: commodity avg `-0.0443` n `13`; crypto_alt avg `-0.118` n `239`; crypto_major avg `0.1258` n `8`; equity avg `0.1779` n `158`; fx avg `0.0049` n `6`; index avg `0.0016` n `27`; metal avg `-0.0071` n `20`; unknown avg `0.8235` n `1255`
- 4h: commodity avg `-0.058` n `13`; crypto_alt avg `-0.057` n `239`; crypto_major avg `0.1621` n `8`; equity avg `-0.0387` n `158`; fx avg `0.0023` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0091` n `20`; unknown avg `-0.2167` n `1233`
- 24h: commodity avg `-0.2128` n `13`; crypto_alt avg `0.7754` n `239`; crypto_major avg `-0.161` n `8`; equity avg `0.6855` n `158`; fx avg `-0.0735` n `6`; index avg `0.0981` n `27`; metal avg `0.0287` n `20`; unknown avg `8.0536` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
