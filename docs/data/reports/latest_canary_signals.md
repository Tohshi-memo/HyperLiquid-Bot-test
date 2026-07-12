# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T07:22:25.154471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.0429` n `230`; crypto_major avg `0.0707` n `8`; equity avg `0.0132` n `92`; fx avg `-0.0029` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0038` n `765`
- 1h: commodity avg `0.0908` n `12`; crypto_alt avg `0.2218` n `230`; crypto_major avg `0.3069` n `8`; equity avg `-0.0035` n `92`; fx avg `0.0018` n `6`; index avg `-0.0153` n `25`; metal avg `0.0002` n `20`; unknown avg `2.942` n `763`
- 4h: commodity avg `0.0849` n `12`; crypto_alt avg `-0.3357` n `230`; crypto_major avg `-0.3115` n `8`; equity avg `-0.1594` n `92`; fx avg `0.0015` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0186` n `20`; unknown avg `-0.1415` n `747`
- 24h: commodity avg `0.4719` n `12`; crypto_alt avg `-0.6317` n `230`; crypto_major avg `-0.6757` n `8`; equity avg `-0.2178` n `92`; fx avg `0.0029` n `6`; index avg `-0.1534` n `25`; metal avg `-0.0992` n `20`; unknown avg `0.052` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
