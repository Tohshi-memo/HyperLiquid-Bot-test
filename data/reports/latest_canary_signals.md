# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T17:52:27.597824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0621` n `13`; crypto_alt avg `0.009` n `239`; crypto_major avg `0.0138` n `8`; equity avg `-0.2442` n `158`; fx avg `-0.0231` n `6`; index avg `-0.006` n `27`; metal avg `0.0047` n `20`; unknown avg `0.4424` n `1257`
- 1h: commodity avg `-0.0293` n `13`; crypto_alt avg `-0.5713` n `239`; crypto_major avg `-0.6652` n `8`; equity avg `-1.2439` n `158`; fx avg `-0.0281` n `6`; index avg `-0.1641` n `27`; metal avg `-0.1123` n `20`; unknown avg `11.043` n `1255`
- 4h: commodity avg `-0.2255` n `13`; crypto_alt avg `-0.3046` n `239`; crypto_major avg `-0.4184` n `8`; equity avg `-1.8177` n `158`; fx avg `-0.0048` n `6`; index avg `-0.1522` n `27`; metal avg `0.0277` n `20`; unknown avg `6.5949` n `1243`
- 24h: commodity avg `-0.021` n `13`; crypto_alt avg `2.2289` n `239`; crypto_major avg `-0.4745` n `8`; equity avg `1.175` n `158`; fx avg `-0.1384` n `6`; index avg `0.0702` n `27`; metal avg `-0.2699` n `20`; unknown avg `54.0409` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
