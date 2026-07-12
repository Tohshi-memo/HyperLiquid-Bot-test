# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T08:37:27.742351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `-0.0042` n `230`; crypto_major avg `-0.0423` n `8`; equity avg `0.0105` n `92`; fx avg `-0.0061` n `6`; index avg `0.0137` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0027` n `765`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `0.2062` n `230`; crypto_major avg `0.2218` n `8`; equity avg `0.0132` n `92`; fx avg `-0.0001` n `6`; index avg `0.0219` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.0654` n `765`
- 4h: commodity avg `0.0696` n `12`; crypto_alt avg `-0.2` n `230`; crypto_major avg `-0.0112` n `8`; equity avg `-0.1018` n `92`; fx avg `0.0029` n `6`; index avg `0.0028` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.13` n `747`
- 24h: commodity avg `0.4595` n `12`; crypto_alt avg `-0.637` n `230`; crypto_major avg `-0.6425` n `8`; equity avg `-0.1788` n `92`; fx avg `-0.0037` n `6`; index avg `-0.1051` n `25`; metal avg `-0.1093` n `20`; unknown avg `-0.0279` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
