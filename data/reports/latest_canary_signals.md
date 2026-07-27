# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T18:07:27.608282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0768` n `12`; crypto_alt avg `0.0229` n `230`; crypto_major avg `0.0086` n `8`; equity avg `0.1566` n `102`; fx avg `0.0137` n `6`; index avg `0.0377` n `25`; metal avg `0.0114` n `20`; unknown avg `-0.0143` n `774`
- 1h: commodity avg `-0.0755` n `12`; crypto_alt avg `-0.0472` n `230`; crypto_major avg `-0.0884` n `8`; equity avg `0.199` n `102`; fx avg `0.0112` n `6`; index avg `0.0746` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.1848` n `774`
- 4h: commodity avg `-0.344` n `12`; crypto_alt avg `-1.2147` n `230`; crypto_major avg `-0.9667` n `8`; equity avg `-0.8991` n `102`; fx avg `-0.0831` n `6`; index avg `-0.2369` n `25`; metal avg `0.0287` n `20`; unknown avg `-0.5283` n `774`
- 24h: commodity avg `-0.7765` n `12`; crypto_alt avg `-1.0289` n `230`; crypto_major avg `-0.2725` n `8`; equity avg `-1.6808` n `102`; fx avg `-0.0081` n `6`; index avg `-0.4779` n `25`; metal avg `0.188` n `20`; unknown avg `-0.412` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
