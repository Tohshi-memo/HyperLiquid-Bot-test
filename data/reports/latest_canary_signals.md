# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T06:22:26.105028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `0.2796` n `239`; crypto_major avg `0.1359` n `8`; equity avg `0.055` n `158`; fx avg `-0.0215` n `6`; index avg `-0.0066` n `27`; metal avg `0.0194` n `20`; unknown avg `11.8429` n `1250`
- 1h: commodity avg `0.147` n `13`; crypto_alt avg `0.1727` n `239`; crypto_major avg `0.0238` n `8`; equity avg `-0.1174` n `158`; fx avg `-0.0405` n `6`; index avg `-0.0374` n `27`; metal avg `0.0631` n `20`; unknown avg `-0.1466` n `1228`
- 4h: commodity avg `0.0242` n `13`; crypto_alt avg `-0.0173` n `239`; crypto_major avg `-0.8725` n `8`; equity avg `-0.8556` n `158`; fx avg `-0.0375` n `6`; index avg `-0.1118` n `27`; metal avg `-0.2042` n `20`; unknown avg `-0.1131` n `1220`
- 24h: commodity avg `1.495` n `13`; crypto_alt avg `-4.3096` n `239`; crypto_major avg `-5.8893` n `8`; equity avg `-6.0552` n `158`; fx avg `0.0069` n `6`; index avg `-0.7963` n `27`; metal avg `-0.4757` n `20`; unknown avg `231.6437` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
