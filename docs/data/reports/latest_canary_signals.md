# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T03:37:26.159061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `0.1821` n `237`; crypto_major avg `0.1254` n `8`; equity avg `0.0337` n `151`; fx avg `-0.0088` n `6`; index avg `0.0005` n `26`; metal avg `0.0064` n `20`; unknown avg `0.1684` n `1193`
- 1h: commodity avg `0.0131` n `13`; crypto_alt avg `0.2274` n `237`; crypto_major avg `0.2222` n `8`; equity avg `0.0571` n `151`; fx avg `-0.0145` n `6`; index avg `0.008` n `26`; metal avg `0.0169` n `20`; unknown avg `0.0188` n `1191`
- 4h: commodity avg `0.0409` n `13`; crypto_alt avg `0.2074` n `236`; crypto_major avg `0.8178` n `8`; equity avg `0.0999` n `151`; fx avg `-0.0193` n `6`; index avg `0.0205` n `26`; metal avg `0.0379` n `20`; unknown avg `3.5819` n `1185`
- 24h: commodity avg `-0.0954` n `13`; crypto_alt avg `-2.4367` n `236`; crypto_major avg `-0.4545` n `8`; equity avg `-0.9499` n `151`; fx avg `-0.0502` n `6`; index avg `-0.1043` n `26`; metal avg `-0.0646` n `20`; unknown avg `3.6293` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1654`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1374`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0776`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
