# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T01:07:27.987470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.0868` n `236`; crypto_major avg `0.0299` n `8`; equity avg `0.2039` n `151`; fx avg `0.0078` n `6`; index avg `0.0208` n `26`; metal avg `0.002` n `20`; unknown avg `2.5234` n `1191`
- 1h: commodity avg `0.0312` n `13`; crypto_alt avg `-0.3068` n `236`; crypto_major avg `-0.232` n `8`; equity avg `0.151` n `151`; fx avg `-0.0112` n `6`; index avg `0.0059` n `26`; metal avg `-0.0177` n `20`; unknown avg `1.1821` n `1191`
- 4h: commodity avg `0.0421` n `13`; crypto_alt avg `0.3524` n `236`; crypto_major avg `0.016` n `8`; equity avg `-0.0458` n `151`; fx avg `-0.005` n `6`; index avg `-0.0117` n `26`; metal avg `-0.0081` n `20`; unknown avg `1.1097` n `1183`
- 24h: commodity avg `0.5347` n `13`; crypto_alt avg `-1.5829` n `236`; crypto_major avg `-1.3515` n `8`; equity avg `-3.6672` n `151`; fx avg `-0.041` n `6`; index avg `-0.6061` n `26`; metal avg `-0.0015` n `20`; unknown avg `40.1556` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1699`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
