# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T19:29:54.108260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.5687` n `237`; crypto_major avg `-0.4605` n `8`; equity avg `-0.0814` n `151`; fx avg `-0.0059` n `6`; index avg `0.0008` n `26`; metal avg `-0.0073` n `20`; unknown avg `0.5426` n `1194`
- 1h: commodity avg `0.0134` n `13`; crypto_alt avg `-0.6027` n `237`; crypto_major avg `-0.3224` n `8`; equity avg `-0.088` n `151`; fx avg `-0.0032` n `6`; index avg `0.0001` n `26`; metal avg `0.0033` n `20`; unknown avg `4.4312` n `1176`
- 4h: commodity avg `0.0163` n `13`; crypto_alt avg `-1.0449` n `237`; crypto_major avg `-0.5982` n `8`; equity avg `-0.2383` n `151`; fx avg `0.0072` n `6`; index avg `-0.0327` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.4242` n `1144`
- 24h: commodity avg `-0.0179` n `13`; crypto_alt avg `-4.2283` n `236`; crypto_major avg `-1.8221` n `8`; equity avg `-1.1669` n `151`; fx avg `0.0001` n `6`; index avg `-0.1507` n `26`; metal avg `-0.0449` n `20`; unknown avg `0.8064` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2105`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1349`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
