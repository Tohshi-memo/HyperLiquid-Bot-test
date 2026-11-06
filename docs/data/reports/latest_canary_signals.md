# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T17:07:28.875090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0544` n `13`; crypto_alt avg `0.0563` n `239`; crypto_major avg `0.0007` n `8`; equity avg `-0.1822` n `158`; fx avg `-0.0046` n `6`; index avg `-0.0333` n `27`; metal avg `-0.0588` n `20`; unknown avg `0.3265` n `1251`
- 1h: commodity avg `0.0677` n `13`; crypto_alt avg `0.2827` n `239`; crypto_major avg `0.3594` n `8`; equity avg `0.3707` n `158`; fx avg `0.0009` n `6`; index avg `0.0205` n `27`; metal avg `-0.0526` n `20`; unknown avg `96.6362` n `1255`
- 4h: commodity avg `-0.2801` n `13`; crypto_alt avg `0.41` n `239`; crypto_major avg `0.3351` n `8`; equity avg `-0.5039` n `158`; fx avg `-0.0248` n `6`; index avg `0.0449` n `27`; metal avg `-0.0273` n `20`; unknown avg `53.4503` n `1243`
- 24h: commodity avg `0.1024` n `13`; crypto_alt avg `2.9726` n `239`; crypto_major avg `-0.0987` n `8`; equity avg `1.9744` n `158`; fx avg `-0.1051` n `6`; index avg `0.1423` n `27`; metal avg `-0.3894` n `20`; unknown avg `63.2924` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
