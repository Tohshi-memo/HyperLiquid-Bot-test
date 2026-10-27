# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T07:37:28.572074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `0.1036` n `238`; crypto_major avg `0.0084` n `8`; equity avg `0.0105` n `154`; fx avg `-0.0038` n `6`; index avg `0.001` n `27`; metal avg `-0.0453` n `20`; unknown avg `-0.0483` n `1238`
- 1h: commodity avg `0.1476` n `13`; crypto_alt avg `0.2846` n `237`; crypto_major avg `0.02` n `8`; equity avg `-0.1732` n `154`; fx avg `-0.0104` n `6`; index avg `-0.0362` n `27`; metal avg `-0.0483` n `20`; unknown avg `64.7287` n `1224`
- 4h: commodity avg `0.2333` n `13`; crypto_alt avg `0.2347` n `237`; crypto_major avg `-0.2959` n `8`; equity avg `-1.275` n `154`; fx avg `-0.0403` n `6`; index avg `-0.0648` n `27`; metal avg `-0.3044` n `20`; unknown avg `79.8374` n `1194`
- 24h: commodity avg `0.2087` n `13`; crypto_alt avg `0.7732` n `237`; crypto_major avg `0.4345` n `8`; equity avg `0.4793` n `153`; fx avg `-0.0244` n `6`; index avg `0.0614` n `27`; metal avg `-0.3471` n `20`; unknown avg `1124.0648` n `980`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
