# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T16:07:30.039364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2192` n `13`; crypto_alt avg `0.4527` n `235`; crypto_major avg `0.3009` n `8`; equity avg `0.0461` n `150`; fx avg `0.0217` n `6`; index avg `0.0112` n `26`; metal avg `0.0595` n `20`; unknown avg `0.0712` n `1068`
- 1h: commodity avg `-0.3739` n `13`; crypto_alt avg `1.096` n `235`; crypto_major avg `0.647` n `8`; equity avg `0.3082` n `150`; fx avg `0.0096` n `6`; index avg `0.1062` n `26`; metal avg `0.1013` n `20`; unknown avg `2.1554` n `1068`
- 4h: commodity avg `-0.2585` n `13`; crypto_alt avg `0.3031` n `235`; crypto_major avg `-0.029` n `8`; equity avg `0.1367` n `150`; fx avg `0.023` n `6`; index avg `0.0157` n `26`; metal avg `-0.0767` n `20`; unknown avg `0.0244` n `1022`
- 24h: commodity avg `0.7029` n `13`; crypto_alt avg `-4.8222` n `235`; crypto_major avg `-3.4379` n `8`; equity avg `-1.5822` n `150`; fx avg `-0.1559` n `6`; index avg `-0.3166` n `26`; metal avg `-0.5915` n `20`; unknown avg `15.8584` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
