# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T14:52:31.806135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2222` n `13`; crypto_alt avg `0.2997` n `237`; crypto_major avg `0.2586` n `8`; equity avg `0.8546` n `153`; fx avg `0.0165` n `6`; index avg `0.0962` n `26`; metal avg `0.0712` n `20`; unknown avg `1.4743` n `1220`
- 1h: commodity avg `-0.0479` n `13`; crypto_alt avg `0.7642` n `237`; crypto_major avg `0.7024` n `8`; equity avg `0.9886` n `153`; fx avg `0.037` n `6`; index avg `0.1607` n `26`; metal avg `0.2358` n `20`; unknown avg `616.4585` n `1174`
- 4h: commodity avg `0.1272` n `13`; crypto_alt avg `0.6324` n `237`; crypto_major avg `0.2089` n `8`; equity avg `1.2389` n `152`; fx avg `0.0301` n `6`; index avg `0.2586` n `26`; metal avg `0.0834` n `20`; unknown avg `626.8376` n `1156`
- 24h: commodity avg `-0.3185` n `13`; crypto_alt avg `0.6018` n `237`; crypto_major avg `0.2468` n `8`; equity avg `0.5787` n `152`; fx avg `0.0544` n `6`; index avg `0.2061` n `26`; metal avg `0.1607` n `20`; unknown avg `185.2466` n `918`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2312`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1976`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1928`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1796`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1329`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `669`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0783`, n `669`, weak_sample_signal
