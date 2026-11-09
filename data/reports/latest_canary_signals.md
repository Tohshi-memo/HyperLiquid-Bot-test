# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T02:22:23.763000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.0365` n `239`; crypto_major avg `0.0598` n `8`; equity avg `0.2358` n `158`; fx avg `-0.0095` n `6`; index avg `0.0177` n `27`; metal avg `-0.0555` n `20`; unknown avg `-0.0944` n `1262`
- 1h: commodity avg `0.0916` n `13`; crypto_alt avg `0.5414` n `239`; crypto_major avg `0.6003` n `8`; equity avg `1.5461` n `158`; fx avg `-0.0408` n `6`; index avg `0.1337` n `27`; metal avg `0.1233` n `20`; unknown avg `0.3078` n `1250`
- 4h: commodity avg `-0.161` n `13`; crypto_alt avg `1.5093` n `239`; crypto_major avg `0.8047` n `8`; equity avg `1.4459` n `158`; fx avg `-0.0591` n `6`; index avg `0.1957` n `27`; metal avg `0.6263` n `20`; unknown avg `1.4279` n `1220`
- 24h: commodity avg `-0.0461` n `13`; crypto_alt avg `-1.5315` n `239`; crypto_major avg `-1.7929` n `8`; equity avg `0.8412` n `158`; fx avg `-0.0644` n `6`; index avg `0.103` n `27`; metal avg `0.5302` n `20`; unknown avg `1.2798` n `994`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
