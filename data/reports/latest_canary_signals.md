# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T17:37:26.709055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `-0.0762` n `237`; crypto_major avg `0.0169` n `8`; equity avg `-0.045` n `151`; fx avg `-0.0043` n `6`; index avg `-0.0163` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.2722` n `1194`
- 1h: commodity avg `0.0067` n `13`; crypto_alt avg `0.0532` n `237`; crypto_major avg `0.2259` n `8`; equity avg `-0.0867` n `151`; fx avg `0.0056` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0007` n `20`; unknown avg `-0.4301` n `1192`
- 4h: commodity avg `0.0171` n `13`; crypto_alt avg `-0.9983` n `237`; crypto_major avg `-0.4749` n `8`; equity avg `-0.3593` n `151`; fx avg `-0.0032` n `6`; index avg `-0.0768` n `26`; metal avg `-0.0259` n `20`; unknown avg `-0.7824` n `1161`
- 24h: commodity avg `-0.0003` n `13`; crypto_alt avg `-2.606` n `236`; crypto_major avg `-0.916` n `8`; equity avg `-0.9029` n `151`; fx avg `-0.009` n `6`; index avg `-0.1148` n `26`; metal avg `-0.0335` n `20`; unknown avg `0.5279` n `1017`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1294`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
