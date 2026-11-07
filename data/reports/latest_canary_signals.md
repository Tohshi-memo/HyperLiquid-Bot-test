# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T16:52:26.798726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.0991` n `239`; crypto_major avg `-0.0859` n `8`; equity avg `-0.0231` n `158`; fx avg `0.0156` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0014` n `20`; unknown avg `-0.3248` n `1261`
- 1h: commodity avg `0.0344` n `13`; crypto_alt avg `0.1008` n `239`; crypto_major avg `0.0715` n `8`; equity avg `-0.004` n `158`; fx avg `0.0004` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0018` n `20`; unknown avg `-0.6586` n `1249`
- 4h: commodity avg `0.0514` n `13`; crypto_alt avg `-0.2479` n `239`; crypto_major avg `-0.2308` n `8`; equity avg `-0.1781` n `158`; fx avg `-0.0314` n `6`; index avg `0.0153` n `27`; metal avg `-0.0217` n `20`; unknown avg `-0.6421` n `1241`
- 24h: commodity avg `0.2292` n `13`; crypto_alt avg `-1.9717` n `239`; crypto_major avg `-1.1058` n `8`; equity avg `-0.1547` n `158`; fx avg `-0.0016` n `6`; index avg `-0.0597` n `27`; metal avg `-0.0257` n `20`; unknown avg `-0.9795` n `1111`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
