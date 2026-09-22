# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T10:52:31.895914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0504` n `12`; crypto_alt avg `-0.0056` n `234`; crypto_major avg `0.1015` n `8`; equity avg `0.085` n `140`; fx avg `-0.0078` n `6`; index avg `0.0255` n `26`; metal avg `0.0086` n `20`; unknown avg `-0.2016` n `944`
- 1h: commodity avg `-0.1491` n `12`; crypto_alt avg `-0.6094` n `234`; crypto_major avg `-0.3047` n `8`; equity avg `0.1512` n `140`; fx avg `0.007` n `6`; index avg `0.0175` n `26`; metal avg `0.0408` n `20`; unknown avg `0.777` n `940`
- 4h: commodity avg `-0.7311` n `12`; crypto_alt avg `-0.5199` n `234`; crypto_major avg `-0.0131` n `8`; equity avg `0.4509` n `140`; fx avg `-0.1235` n `6`; index avg `0.0698` n `26`; metal avg `0.1497` n `20`; unknown avg `3.3321` n `934`
- 24h: commodity avg `-0.6233` n `12`; crypto_alt avg `0.2457` n `234`; crypto_major avg `1.7182` n `8`; equity avg `1.0906` n `140`; fx avg `-0.2717` n `6`; index avg `0.2793` n `26`; metal avg `-0.0268` n `20`; unknown avg `1130.0763` n `790`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
