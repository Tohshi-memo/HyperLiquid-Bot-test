# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T10:07:26.698656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0631` n `13`; crypto_alt avg `0.0072` n `235`; crypto_major avg `-0.0135` n `8`; equity avg `0.0134` n `151`; fx avg `0.0028` n `6`; index avg `0.0083` n `26`; metal avg `0.0056` n `20`; unknown avg `0.7894` n `1133`
- 1h: commodity avg `-0.093` n `13`; crypto_alt avg `-0.526` n `235`; crypto_major avg `-0.1387` n `8`; equity avg `-0.1037` n `151`; fx avg `-0.0123` n `6`; index avg `0.0031` n `26`; metal avg `-0.0084` n `20`; unknown avg `1.7134` n `1133`
- 4h: commodity avg `-0.2211` n `13`; crypto_alt avg `-0.9269` n `235`; crypto_major avg `-0.477` n `8`; equity avg `0.2879` n `151`; fx avg `-0.0621` n `6`; index avg `0.1057` n `26`; metal avg `0.0049` n `20`; unknown avg `0.6253` n `1117`
- 24h: commodity avg `-0.0163` n `13`; crypto_alt avg `-4.1315` n `235`; crypto_major avg `-2.2981` n `8`; equity avg `-2.837` n `151`; fx avg `0.0239` n `6`; index avg `-0.3341` n `26`; metal avg `0.0024` n `20`; unknown avg `0.1272` n `973`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1826`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1653`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1643`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1431`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.075`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0731`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
