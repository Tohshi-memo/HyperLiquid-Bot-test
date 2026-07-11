# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T14:37:24.339971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `0.2259` n `230`; crypto_major avg `0.3061` n `8`; equity avg `0.077` n `92`; fx avg `-0.0055` n `6`; index avg `0.0048` n `25`; metal avg `0.0046` n `20`; unknown avg `0.0573` n `765`
- 1h: commodity avg `-0.0352` n `12`; crypto_alt avg `0.3036` n `230`; crypto_major avg `0.4517` n `8`; equity avg `0.0077` n `92`; fx avg `-0.0045` n `6`; index avg `0.0028` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.0624` n `765`
- 4h: commodity avg `-0.0356` n `12`; crypto_alt avg `0.6721` n `230`; crypto_major avg `0.7088` n `8`; equity avg `-0.04` n `92`; fx avg `-0.0071` n `6`; index avg `-0.0004` n `25`; metal avg `-0.014` n `20`; unknown avg `-0.1074` n `765`
- 24h: commodity avg `0.0517` n `12`; crypto_alt avg `1.6017` n `229`; crypto_major avg `1.0986` n `8`; equity avg `0.5137` n `92`; fx avg `-0.0423` n `6`; index avg `0.1344` n `25`; metal avg `0.1434` n `20`; unknown avg `3.016` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
