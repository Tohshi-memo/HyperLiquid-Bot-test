# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T00:07:25.242817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `0.2457` n `236`; crypto_major avg `0.1989` n `8`; equity avg `0.4338` n `151`; fx avg `0.0211` n `6`; index avg `0.0444` n `26`; metal avg `0.0373` n `20`; unknown avg `0.44` n `1128`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `0.1515` n `236`; crypto_major avg `0.1465` n `8`; equity avg `-0.1002` n `151`; fx avg `0.0533` n `6`; index avg `-0.0798` n `26`; metal avg `0.0752` n `20`; unknown avg `1.4159` n `1128`
- 4h: commodity avg `-0.0281` n `13`; crypto_alt avg `0.3568` n `236`; crypto_major avg `-0.0475` n `8`; equity avg `-1.2301` n `151`; fx avg `0.0717` n `6`; index avg `-0.2021` n `26`; metal avg `0.0771` n `20`; unknown avg `1.6055` n `1018`
- 24h: commodity avg `-0.1381` n `13`; crypto_alt avg `-2.12` n `236`; crypto_major avg `-1.8371` n `8`; equity avg `-5.3333` n `151`; fx avg `-0.0402` n `6`; index avg `-0.7566` n `26`; metal avg `-0.7669` n `20`; unknown avg `1393.8909` n `890`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0996`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.082`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0617`, n `666`, weak_sample_signal
