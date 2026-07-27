# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T19:22:29.297536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0187` n `230`; crypto_major avg `0.0411` n `8`; equity avg `0.0745` n `102`; fx avg `-0.0052` n `6`; index avg `0.0141` n `25`; metal avg `0.0503` n `20`; unknown avg `1182.9194` n `774`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1139` n `230`; crypto_major avg `0.2359` n `8`; equity avg `0.7695` n `102`; fx avg `-0.0023` n `6`; index avg `0.1465` n `25`; metal avg `0.112` n `20`; unknown avg `1183.2577` n `774`
- 4h: commodity avg `-0.17` n `12`; crypto_alt avg `0.0173` n `230`; crypto_major avg `0.1214` n `8`; equity avg `0.6429` n `102`; fx avg `-0.0306` n `6`; index avg `0.059` n `25`; metal avg `0.0078` n `20`; unknown avg `1182.6683` n `774`
- 24h: commodity avg `-0.9879` n `12`; crypto_alt avg `-1.0591` n `230`; crypto_major avg `-0.2894` n `8`; equity avg `-1.0919` n `102`; fx avg `-0.0231` n `6`; index avg `-0.3262` n `25`; metal avg `0.2205` n `20`; unknown avg `1209.3214` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
