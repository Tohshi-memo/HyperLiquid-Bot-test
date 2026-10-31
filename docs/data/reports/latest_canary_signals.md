# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T07:52:28.235038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `13`; crypto_alt avg `-0.1291` n `238`; crypto_major avg `-0.0399` n `8`; equity avg `-0.0642` n `156`; fx avg `0.0036` n `6`; index avg `-0.0015` n `27`; metal avg `-0.018` n `20`; unknown avg `-0.0197` n `1262`
- 1h: commodity avg `-0.0066` n `13`; crypto_alt avg `-0.5767` n `238`; crypto_major avg `-0.3332` n `8`; equity avg `-0.0914` n `156`; fx avg `0.0099` n `6`; index avg `0.0004` n `27`; metal avg `-0.0399` n `20`; unknown avg `4.9572` n `1256`
- 4h: commodity avg `-0.0381` n `13`; crypto_alt avg `-0.8427` n `238`; crypto_major avg `-0.3821` n `8`; equity avg `-0.1003` n `156`; fx avg `0.0081` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0106` n `20`; unknown avg `0.9995` n `1222`
- 24h: commodity avg `-0.2468` n `13`; crypto_alt avg `0.7639` n `238`; crypto_major avg `-0.9359` n `8`; equity avg `-2.2177` n `156`; fx avg `-0.0678` n `6`; index avg `-0.2154` n `27`; metal avg `-0.3686` n `20`; unknown avg `4.6408` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
