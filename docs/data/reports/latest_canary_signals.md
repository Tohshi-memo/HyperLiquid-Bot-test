# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T11:22:27.291268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `13`; crypto_alt avg `0.1282` n `239`; crypto_major avg `0.0918` n `8`; equity avg `0.2483` n `158`; fx avg `0.0292` n `6`; index avg `0.0248` n `27`; metal avg `0.0545` n `20`; unknown avg `30.0752` n `1257`
- 1h: commodity avg `0.2261` n `13`; crypto_alt avg `0.0499` n `239`; crypto_major avg `0.0682` n `8`; equity avg `0.0616` n `158`; fx avg `0.0583` n `6`; index avg `-0.0005` n `27`; metal avg `0.0325` n `20`; unknown avg `0.9958` n `1242`
- 4h: commodity avg `-0.0948` n `13`; crypto_alt avg `1.1545` n `239`; crypto_major avg `0.939` n `8`; equity avg `1.7144` n `158`; fx avg `0.0281` n `6`; index avg `0.2362` n `27`; metal avg `0.1821` n `20`; unknown avg `21.8432` n `1184`
- 24h: commodity avg `0.85` n `13`; crypto_alt avg `-3.2178` n `239`; crypto_major avg `-5.3584` n `8`; equity avg `-4.7394` n `158`; fx avg `0.0086` n `6`; index avg `-0.6438` n `27`; metal avg `-0.4413` n `20`; unknown avg `16.1045` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
