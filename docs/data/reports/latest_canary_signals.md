# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T00:52:24.595536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0473` n `13`; crypto_alt avg `-0.2416` n `237`; crypto_major avg `-0.0641` n `8`; equity avg `0.1013` n `154`; fx avg `0.0116` n `6`; index avg `0.0273` n `27`; metal avg `0.01` n `20`; unknown avg `0.2559` n `1238`
- 1h: commodity avg `-0.0263` n `13`; crypto_alt avg `-0.0397` n `237`; crypto_major avg `0.2739` n `8`; equity avg `0.3337` n `154`; fx avg `0.0116` n `6`; index avg `0.0709` n `27`; metal avg `0.017` n `20`; unknown avg `0.3001` n `1228`
- 4h: commodity avg `-0.0218` n `13`; crypto_alt avg `0.5182` n `237`; crypto_major avg `0.7727` n `8`; equity avg `0.7057` n `154`; fx avg `0.0112` n `6`; index avg `0.1638` n `27`; metal avg `-0.0094` n `20`; unknown avg `134.0371` n `1202`
- 24h: commodity avg `-0.0393` n `13`; crypto_alt avg `0.431` n `237`; crypto_major avg `0.8339` n `8`; equity avg `1.9853` n `153`; fx avg `-0.0267` n `6`; index avg `0.1691` n `27`; metal avg `0.036` n `20`; unknown avg `761.2939` n `970`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
