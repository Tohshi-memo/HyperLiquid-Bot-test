# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T09:37:29.205918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `0.2647` n `237`; crypto_major avg `0.2886` n `8`; equity avg `0.0487` n `151`; fx avg `0.0014` n `6`; index avg `0.002` n `26`; metal avg `0.0135` n `20`; unknown avg `0.0655` n `1193`
- 1h: commodity avg `-0.0018` n `13`; crypto_alt avg `0.7052` n `237`; crypto_major avg `0.6052` n `8`; equity avg `0.2323` n `151`; fx avg `0.0015` n `6`; index avg `0.0285` n `26`; metal avg `0.0158` n `20`; unknown avg `1.6744` n `1095`
- 4h: commodity avg `0.0025` n `13`; crypto_alt avg `0.6993` n `237`; crypto_major avg `0.5586` n `8`; equity avg `0.4385` n `151`; fx avg `-0.0094` n `6`; index avg `0.0747` n `26`; metal avg `0.0136` n `20`; unknown avg `1.3062` n `1063`
- 24h: commodity avg `0.0403` n `13`; crypto_alt avg `-2.0274` n `236`; crypto_major avg `-0.3705` n `8`; equity avg `-0.5553` n `151`; fx avg `-0.0332` n `6`; index avg `-0.0775` n `26`; metal avg `-0.0499` n `20`; unknown avg `4.8993` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1896`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.133`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.082`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
