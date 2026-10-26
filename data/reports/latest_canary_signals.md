# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T21:37:25.853880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.3972` n `237`; crypto_major avg `0.1911` n `8`; equity avg `0.04` n `154`; fx avg `-0.0019` n `6`; index avg `0.0012` n `27`; metal avg `0.0135` n `20`; unknown avg `-0.2875` n `1238`
- 1h: commodity avg `-0.0191` n `13`; crypto_alt avg `0.207` n `237`; crypto_major avg `0.1831` n `8`; equity avg `0.0946` n `154`; fx avg `-0.0055` n `6`; index avg `0.0106` n `27`; metal avg `0.0299` n `20`; unknown avg `1.6347` n `1228`
- 4h: commodity avg `-0.2014` n `13`; crypto_alt avg `-0.6578` n `237`; crypto_major avg `-0.6224` n `8`; equity avg `-0.221` n `154`; fx avg `-0.0395` n `6`; index avg `-0.0309` n `27`; metal avg `-0.067` n `20`; unknown avg `9.246` n `1134`
- 24h: commodity avg `-0.3591` n `13`; crypto_alt avg `-0.2381` n `237`; crypto_major avg `-0.0937` n `8`; equity avg `0.6612` n `153`; fx avg `-0.0181` n `6`; index avg `-0.0967` n `27`; metal avg `0.0189` n `20`; unknown avg `703.3823` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
