# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T02:22:27.266969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `13`; crypto_alt avg `-0.0261` n `237`; crypto_major avg `-0.024` n `8`; equity avg `-0.0068` n `154`; fx avg `0.0054` n `6`; index avg `0.0083` n `27`; metal avg `0.0546` n `20`; unknown avg `1.6715` n `1238`
- 1h: commodity avg `-0.0483` n `13`; crypto_alt avg `-0.1569` n `237`; crypto_major avg `-0.119` n `8`; equity avg `-0.0302` n `154`; fx avg `-0.0142` n `6`; index avg `-0.0084` n `27`; metal avg `0.0593` n `20`; unknown avg `29.1592` n `1236`
- 4h: commodity avg `-0.0875` n `13`; crypto_alt avg `-0.0471` n `237`; crypto_major avg `0.2601` n `8`; equity avg `0.1293` n `154`; fx avg `-0.0269` n `6`; index avg `0.0934` n `27`; metal avg `-0.0374` n `20`; unknown avg `-0.0578` n `1210`
- 24h: commodity avg `-0.0052` n `13`; crypto_alt avg `0.466` n `237`; crypto_major avg `0.8723` n `8`; equity avg `2.021` n `153`; fx avg `-0.0029` n `6`; index avg `0.1339` n `27`; metal avg `0.0489` n `20`; unknown avg `998.3533` n `1004`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
