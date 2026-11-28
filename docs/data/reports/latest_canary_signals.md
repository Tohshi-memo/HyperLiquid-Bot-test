# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T21:52:34.873790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1052` n `13`; crypto_alt avg `0.0285` n `239`; crypto_major avg `0.0751` n `8`; equity avg `0.0117` n `168`; fx avg `0.0095` n `6`; index avg `0.0021` n `27`; metal avg `0.0017` n `20`; unknown avg `5.1045` n `1266`
- 1h: commodity avg `0.1265` n `13`; crypto_alt avg `-0.0639` n `239`; crypto_major avg `-0.0827` n `8`; equity avg `0.0244` n `168`; fx avg `0.0088` n `6`; index avg `0.0046` n `27`; metal avg `0.0048` n `20`; unknown avg `5.2234` n `1224`
- 4h: commodity avg `0.2672` n `13`; crypto_alt avg `-0.055` n `239`; crypto_major avg `0.0471` n `8`; equity avg `0.2374` n `168`; fx avg `0.0043` n `6`; index avg `0.025` n `27`; metal avg `0.0357` n `20`; unknown avg `6.3883` n `1182`
- 24h: commodity avg `0.113` n `13`; crypto_alt avg `-3.544` n `239`; crypto_major avg `-1.3637` n `8`; equity avg `-0.0602` n `168`; fx avg `-0.0063` n `6`; index avg `-0.0315` n `27`; metal avg `0.0351` n `20`; unknown avg `3.1884` n `1085`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
