# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T06:22:33.486135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `-0.0239` n `230`; crypto_major avg `-0.0987` n `8`; equity avg `-0.0195` n `92`; fx avg `0.0` n `6`; index avg `-0.0124` n `25`; metal avg `-0.0048` n `20`; unknown avg `0.051` n `765`
- 1h: commodity avg `-0.0742` n `12`; crypto_alt avg `-0.4176` n `230`; crypto_major avg `-0.3767` n `8`; equity avg `-0.1054` n `92`; fx avg `-0.0022` n `6`; index avg `-0.0246` n `25`; metal avg `-0.0125` n `20`; unknown avg `0.0675` n `749`
- 4h: commodity avg `-0.1454` n `12`; crypto_alt avg `-0.4072` n `230`; crypto_major avg `-0.6194` n `8`; equity avg `-0.1154` n `92`; fx avg `-0.0018` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.2896` n `749`
- 24h: commodity avg `0.4236` n `12`; crypto_alt avg `-1.0232` n `230`; crypto_major avg `-1.0362` n `8`; equity avg `-0.0808` n `92`; fx avg `-0.0135` n `6`; index avg `-0.1097` n `25`; metal avg `-0.1008` n `20`; unknown avg `-0.1045` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
