# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T10:52:30.093140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0564` n `13`; crypto_alt avg `0.0619` n `239`; crypto_major avg `0.1489` n `8`; equity avg `0.0631` n `163`; fx avg `0.0079` n `6`; index avg `0.0096` n `27`; metal avg `0.0112` n `20`; unknown avg `0.1789` n `1264`
- 1h: commodity avg `0.0232` n `13`; crypto_alt avg `0.0107` n `239`; crypto_major avg `-0.1626` n `8`; equity avg `-0.0466` n `163`; fx avg `0.0082` n `6`; index avg `0.0096` n `27`; metal avg `-0.0444` n `20`; unknown avg `3.9751` n `1262`
- 4h: commodity avg `0.067` n `13`; crypto_alt avg `0.3312` n `239`; crypto_major avg `0.1934` n `8`; equity avg `0.5553` n `163`; fx avg `-0.0512` n `6`; index avg `0.1011` n `27`; metal avg `-0.2242` n `20`; unknown avg `87.9834` n `1186`
- 24h: commodity avg `-0.257` n `13`; crypto_alt avg `1.3265` n `239`; crypto_major avg `1.4441` n `8`; equity avg `2.1125` n `163`; fx avg `-0.073` n `6`; index avg `0.19` n `27`; metal avg `-0.9768` n `20`; unknown avg `5.7769` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
