# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T06:07:23.360234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `13`; crypto_alt avg `0.0195` n `239`; crypto_major avg `0.0067` n `8`; equity avg `0.0187` n `158`; fx avg `0.0018` n `6`; index avg `0.0064` n `27`; metal avg `0.0013` n `20`; unknown avg `-0.0104` n `1230`
- 1h: commodity avg `-0.036` n `13`; crypto_alt avg `0.0923` n `239`; crypto_major avg `-0.0049` n `8`; equity avg `0.0834` n `158`; fx avg `0.0159` n `6`; index avg `0.01` n `27`; metal avg `0.0055` n `20`; unknown avg `0.0909` n `1224`
- 4h: commodity avg `-0.045` n `13`; crypto_alt avg `-0.0806` n `239`; crypto_major avg `0.0984` n `8`; equity avg `0.1159` n `158`; fx avg `0.0165` n `6`; index avg `0.0044` n `27`; metal avg `-0.0022` n `20`; unknown avg `-0.0852` n `1210`
- 24h: commodity avg `0.126` n `13`; crypto_alt avg `-1.7462` n `239`; crypto_major avg `-0.6809` n `8`; equity avg `0.0487` n `158`; fx avg `0.0324` n `6`; index avg `0.0373` n `27`; metal avg `-0.0484` n `20`; unknown avg `158.8623` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
