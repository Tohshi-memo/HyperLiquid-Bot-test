# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T11:07:25.548301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `13`; crypto_alt avg `-0.2372` n `235`; crypto_major avg `-0.071` n `8`; equity avg `-0.1949` n `151`; fx avg `0.0072` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0352` n `20`; unknown avg `0.3216` n `1134`
- 1h: commodity avg `-0.0224` n `13`; crypto_alt avg `-0.0128` n `235`; crypto_major avg `0.3565` n `8`; equity avg `-0.1668` n `151`; fx avg `0.0105` n `6`; index avg `-0.0269` n `26`; metal avg `-0.036` n `20`; unknown avg `1.1564` n `1133`
- 4h: commodity avg `0.0531` n `13`; crypto_alt avg `-1.0137` n `235`; crypto_major avg `-0.3458` n `8`; equity avg `-0.4971` n `151`; fx avg `0.0088` n `6`; index avg `-0.0421` n `26`; metal avg `-0.0787` n `20`; unknown avg `1192.9902` n `1037`
- 24h: commodity avg `1.1649` n `13`; crypto_alt avg `0.0329` n `235`; crypto_major avg `0.4704` n `8`; equity avg `-0.2647` n `151`; fx avg `0.0242` n `6`; index avg `0.0004` n `26`; metal avg `-0.4773` n `20`; unknown avg `1268.3339` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1515`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1306`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.075`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0721`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
