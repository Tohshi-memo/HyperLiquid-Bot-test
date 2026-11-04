# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T08:22:25.879499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.73` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.6299` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0742` n `13`; crypto_alt avg `0.0949` n `239`; crypto_major avg `0.0309` n `8`; equity avg `0.1552` n `158`; fx avg `-0.0043` n `6`; index avg `0.0278` n `27`; metal avg `0.0111` n `20`; unknown avg `0.1245` n `1264`
- 1h: commodity avg `-0.0625` n `13`; crypto_alt avg `0.4227` n `239`; crypto_major avg `0.3727` n `8`; equity avg `0.6144` n `158`; fx avg `0.0087` n `6`; index avg `0.102` n `27`; metal avg `0.0763` n `20`; unknown avg `201.2967` n `1242`
- 4h: commodity avg `0.2719` n `13`; crypto_alt avg `2.7541` n `239`; crypto_major avg `1.9931` n `8`; equity avg `3.623` n `158`; fx avg `0.0825` n `6`; index avg `0.5305` n `27`; metal avg `1.0146` n `20`; unknown avg `3.6885` n `1224`
- 24h: commodity avg `-0.2819` n `13`; crypto_alt avg `3.342` n `239`; crypto_major avg `1.9762` n `8`; equity avg `2.8071` n `158`; fx avg `0.1322` n `6`; index avg `0.1813` n `27`; metal avg `0.8883` n `20`; unknown avg `191.4906` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2326`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
