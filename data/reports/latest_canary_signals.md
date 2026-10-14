# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T10:52:30.364346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0828` n `13`; crypto_alt avg `0.1152` n `235`; crypto_major avg `0.0821` n `8`; equity avg `-0.0594` n `151`; fx avg `0.0082` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.0312` n `1136`
- 1h: commodity avg `0.0052` n `13`; crypto_alt avg `0.1005` n `235`; crypto_major avg `0.2409` n `8`; equity avg `-0.088` n `151`; fx avg `0.0078` n `6`; index avg `-0.0363` n `26`; metal avg `-0.0214` n `20`; unknown avg `0.2377` n `1133`
- 4h: commodity avg `0.074` n `13`; crypto_alt avg `-0.6142` n `235`; crypto_major avg `-0.108` n `8`; equity avg `-0.1644` n `151`; fx avg `-0.0213` n `6`; index avg `-0.0243` n `26`; metal avg `-0.0758` n `20`; unknown avg `1192.565` n `1037`
- 24h: commodity avg `1.1899` n `13`; crypto_alt avg `-0.1256` n `235`; crypto_major avg `0.3007` n `8`; equity avg `-0.7615` n `151`; fx avg `0.0193` n `6`; index avg `-0.0001` n `26`; metal avg `-0.4303` n `20`; unknown avg `1267.9443` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1514`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1307`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.075`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
