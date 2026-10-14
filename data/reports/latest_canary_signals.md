# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T21:37:31.320752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `13`; crypto_alt avg `0.4658` n `236`; crypto_major avg `0.4023` n `8`; equity avg `-0.0632` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0181` n `26`; metal avg `0.0061` n `20`; unknown avg `0.5343` n `1136`
- 1h: commodity avg `-0.0172` n `13`; crypto_alt avg `0.4442` n `236`; crypto_major avg `0.2133` n `8`; equity avg `-0.2967` n `151`; fx avg `-0.0123` n `6`; index avg `-0.0098` n `26`; metal avg `0.0161` n `20`; unknown avg `8.2853` n `1126`
- 4h: commodity avg `0.0145` n `13`; crypto_alt avg `0.4416` n `236`; crypto_major avg `0.152` n `8`; equity avg `-0.6309` n `151`; fx avg `-0.01` n `6`; index avg `-0.0629` n `26`; metal avg `-0.0136` n `20`; unknown avg `1.7211` n `1078`
- 24h: commodity avg `-0.0965` n `13`; crypto_alt avg `-2.2877` n `236`; crypto_major avg `-1.8759` n `8`; equity avg `-4.5758` n `151`; fx avg `-0.1307` n `6`; index avg `-0.6051` n `26`; metal avg `-0.8548` n `20`; unknown avg `1309.554` n `946`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.086`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0685`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0682`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0529`, n `666`, weak_sample_signal
