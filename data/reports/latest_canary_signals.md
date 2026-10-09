# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T01:22:31.712734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `13`; crypto_alt avg `0.3163` n `235`; crypto_major avg `0.0136` n `8`; equity avg `0.0014` n `150`; fx avg `-0.016` n `6`; index avg `-0.0007` n `26`; metal avg `0.0976` n `20`; unknown avg `0.3905` n `1078`
- 1h: commodity avg `-0.0444` n `13`; crypto_alt avg `0.4386` n `235`; crypto_major avg `0.1064` n `8`; equity avg `0.0117` n `150`; fx avg `-0.0036` n `6`; index avg `0.0029` n `26`; metal avg `0.2007` n `20`; unknown avg `0.4827` n `1076`
- 4h: commodity avg `-0.0851` n `13`; crypto_alt avg `0.1416` n `235`; crypto_major avg `-0.1546` n `8`; equity avg `0.0556` n `150`; fx avg `0.036` n `6`; index avg `0.0239` n `26`; metal avg `0.3265` n `20`; unknown avg `0.5313` n `1069`
- 24h: commodity avg `0.4183` n `13`; crypto_alt avg `-3.3778` n `235`; crypto_major avg `-3.7273` n `8`; equity avg `-2.7185` n `150`; fx avg `0.1439` n `6`; index avg `-0.3005` n `26`; metal avg `0.0582` n `20`; unknown avg `6.2109` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
