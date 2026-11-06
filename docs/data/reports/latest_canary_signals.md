# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T21:22:34.040589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `0.2104` n `239`; crypto_major avg `0.1308` n `8`; equity avg `-0.0251` n `158`; fx avg `0.0018` n `6`; index avg `-0.0072` n `27`; metal avg `-0.0095` n `20`; unknown avg `0.5046` n `1253`
- 1h: commodity avg `-0.1008` n `13`; crypto_alt avg `0.1966` n `239`; crypto_major avg `0.1256` n `8`; equity avg `0.0196` n `158`; fx avg `0.0119` n `6`; index avg `-0.0113` n `27`; metal avg `0.009` n `20`; unknown avg `70.3031` n `1221`
- 4h: commodity avg `0.0896` n `13`; crypto_alt avg `-0.2713` n `239`; crypto_major avg `-0.3341` n `8`; equity avg `-0.0167` n `158`; fx avg `0.0194` n `6`; index avg `-0.0744` n `27`; metal avg `0.0277` n `20`; unknown avg `13.275` n `1213`
- 24h: commodity avg `0.078` n `13`; crypto_alt avg `2.0277` n `239`; crypto_major avg `0.0581` n `8`; equity avg `3.1219` n `158`; fx avg `-0.0676` n `6`; index avg `0.4269` n `27`; metal avg `-0.0037` n `20`; unknown avg `54.7644` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
