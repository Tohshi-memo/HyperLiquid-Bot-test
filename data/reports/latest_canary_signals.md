# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T11:22:26.028983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0425` n `13`; crypto_alt avg `-0.2475` n `238`; crypto_major avg `-0.1465` n `8`; equity avg `-0.0496` n `154`; fx avg `0.0084` n `6`; index avg `-0.0188` n `27`; metal avg `-0.018` n `20`; unknown avg `0.1788` n `1216`
- 1h: commodity avg `-0.2865` n `13`; crypto_alt avg `0.6646` n `238`; crypto_major avg `0.6007` n `8`; equity avg `0.7654` n `154`; fx avg `-0.0103` n `6`; index avg `0.1206` n `27`; metal avg `0.0983` n `20`; unknown avg `1.0616` n `1188`
- 4h: commodity avg `-0.3085` n `13`; crypto_alt avg `-0.0641` n `238`; crypto_major avg `0.2333` n `8`; equity avg `1.2473` n `154`; fx avg `-0.0068` n `6`; index avg `0.1813` n `27`; metal avg `0.1097` n `20`; unknown avg `7.2168` n `1156`
- 24h: commodity avg `-0.2319` n `13`; crypto_alt avg `-0.1892` n `237`; crypto_major avg `0.0646` n `8`; equity avg `1.6881` n `153`; fx avg `-0.0472` n `6`; index avg `0.4526` n `27`; metal avg `-0.2074` n `20`; unknown avg `1051.2684` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
