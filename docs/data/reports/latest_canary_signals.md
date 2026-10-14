# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T10:37:28.650354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `13`; crypto_alt avg `0.0583` n `235`; crypto_major avg `0.1049` n `8`; equity avg `-0.0264` n `151`; fx avg `-0.0072` n `6`; index avg `-0.014` n `26`; metal avg `-0.0193` n `20`; unknown avg `-0.0388` n `1135`
- 1h: commodity avg `0.1021` n `13`; crypto_alt avg `0.0581` n `235`; crypto_major avg `0.1665` n `8`; equity avg `0.0518` n `151`; fx avg `-0.0071` n `6`; index avg `-0.0117` n `26`; metal avg `0.0479` n `20`; unknown avg `0.1424` n `1133`
- 4h: commodity avg `0.1278` n `13`; crypto_alt avg `-0.6975` n `235`; crypto_major avg `-0.1867` n `8`; equity avg `-0.1457` n `151`; fx avg `-0.0363` n `6`; index avg `0.033` n `26`; metal avg `-0.084` n `20`; unknown avg `1192.4277` n `1037`
- 24h: commodity avg `1.3164` n `13`; crypto_alt avg `-0.2446` n `235`; crypto_major avg `0.2489` n `8`; equity avg `-0.3376` n `151`; fx avg `0.0148` n `6`; index avg `0.0` n `26`; metal avg `-0.4562` n `20`; unknown avg `1268.0573` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1514`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1307`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0744`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
