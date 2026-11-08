# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T02:37:29.103661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `13`; crypto_alt avg `-0.0469` n `239`; crypto_major avg `-0.0225` n `8`; equity avg `-0.0332` n `158`; fx avg `-0.0049` n `6`; index avg `0.0061` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.0283` n `1260`
- 1h: commodity avg `0.026` n `13`; crypto_alt avg `-0.1499` n `239`; crypto_major avg `-0.1765` n `8`; equity avg `-0.0596` n `158`; fx avg `0.0046` n `6`; index avg `-0.0189` n `27`; metal avg `-0.021` n `20`; unknown avg `-0.1032` n `1254`
- 4h: commodity avg `-0.0378` n `13`; crypto_alt avg `-0.5457` n `239`; crypto_major avg `-0.1389` n `8`; equity avg `0.0211` n `158`; fx avg `0.024` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0202` n `20`; unknown avg `-0.2542` n `1230`
- 24h: commodity avg `0.0997` n `13`; crypto_alt avg `-1.889` n `239`; crypto_major avg `-0.9964` n `8`; equity avg `-0.1734` n `158`; fx avg `0.0043` n `6`; index avg `0.0328` n `27`; metal avg `-0.0528` n `20`; unknown avg `161.1914` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
