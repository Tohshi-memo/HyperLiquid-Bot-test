# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T02:22:36.306597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `-0.2285` n `237`; crypto_major avg `-0.146` n `8`; equity avg `-0.0594` n `151`; fx avg `-0.043` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0311` n `20`; unknown avg `0.235` n `1194`
- 1h: commodity avg `-0.0732` n `13`; crypto_alt avg `0.116` n `237`; crypto_major avg `0.0241` n `8`; equity avg `-0.0369` n `151`; fx avg `-0.0675` n `6`; index avg `-0.0154` n `26`; metal avg `0.073` n `20`; unknown avg `0.0779` n `1192`
- 4h: commodity avg `-0.1616` n `13`; crypto_alt avg `1.6092` n `237`; crypto_major avg `1.1048` n `8`; equity avg `1.6551` n `151`; fx avg `-0.051` n `6`; index avg `0.257` n `26`; metal avg `0.0975` n `20`; unknown avg `3.0409` n `1128`
- 24h: commodity avg `-0.4107` n `13`; crypto_alt avg `-0.1269` n `237`; crypto_major avg `0.6985` n `8`; equity avg `2.2638` n `151`; fx avg `-0.0625` n `6`; index avg `0.4538` n `26`; metal avg `0.275` n `20`; unknown avg `2.9026` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2002`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.144`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1094`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0913`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0622`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0616`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
