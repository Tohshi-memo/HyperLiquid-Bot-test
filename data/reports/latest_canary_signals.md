# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T00:37:25.730136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `13`; crypto_alt avg `0.2679` n `235`; crypto_major avg `0.2152` n `8`; equity avg `0.1275` n `150`; fx avg `0.0094` n `6`; index avg `0.0349` n `26`; metal avg `0.0371` n `20`; unknown avg `0.3675` n `1078`
- 1h: commodity avg `0.0517` n `13`; crypto_alt avg `-0.2849` n `235`; crypto_major avg `-0.1639` n `8`; equity avg `0.1901` n `150`; fx avg `0.0287` n `6`; index avg `0.051` n `26`; metal avg `0.0701` n `20`; unknown avg `0.5262` n `1069`
- 4h: commodity avg `0.0573` n `13`; crypto_alt avg `-0.0241` n `235`; crypto_major avg `0.1387` n `8`; equity avg `0.1706` n `150`; fx avg `0.0424` n `6`; index avg `0.0557` n `26`; metal avg `0.1719` n `20`; unknown avg `0.4537` n `1061`
- 24h: commodity avg `0.5365` n `13`; crypto_alt avg `-3.4493` n `235`; crypto_major avg `-3.5793` n `8`; equity avg `-2.6014` n `150`; fx avg `0.1473` n `6`; index avg `-0.2751` n `26`; metal avg `0.1797` n `20`; unknown avg `6.0047` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
