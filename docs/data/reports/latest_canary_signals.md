# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T00:56:15.533093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0453` n `13`; crypto_alt avg `-0.2185` n `237`; crypto_major avg `-0.0327` n `8`; equity avg `0.1476` n `154`; fx avg `-0.0027` n `6`; index avg `0.0325` n `27`; metal avg `0.0004` n `20`; unknown avg `0.8132` n `1236`
- 1h: commodity avg `-0.0243` n `13`; crypto_alt avg `-0.0166` n `237`; crypto_major avg `0.3054` n `8`; equity avg `0.3801` n `154`; fx avg `-0.0027` n `6`; index avg `0.076` n `27`; metal avg `0.0074` n `20`; unknown avg `0.2877` n `1226`
- 4h: commodity avg `-0.0197` n `13`; crypto_alt avg `0.5414` n `237`; crypto_major avg `0.8043` n `8`; equity avg `0.7525` n `154`; fx avg `-0.003` n `6`; index avg `0.169` n `27`; metal avg `-0.019` n `20`; unknown avg `134.1487` n `1202`
- 24h: commodity avg `-0.0372` n `13`; crypto_alt avg `0.4542` n `237`; crypto_major avg `0.8654` n `8`; equity avg `2.0326` n `153`; fx avg `-0.041` n `6`; index avg `0.1743` n `27`; metal avg `0.0264` n `20`; unknown avg `761.4461` n `970`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
