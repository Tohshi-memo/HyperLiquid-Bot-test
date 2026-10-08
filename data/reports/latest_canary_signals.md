# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T20:22:29.865015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `13`; crypto_alt avg `0.1839` n `235`; crypto_major avg `0.0017` n `8`; equity avg `0.0724` n `150`; fx avg `0.0028` n `6`; index avg `0.009` n `26`; metal avg `0.0093` n `20`; unknown avg `-0.0679` n `1029`
- 1h: commodity avg `-0.1792` n `13`; crypto_alt avg `0.8189` n `235`; crypto_major avg `0.4051` n `8`; equity avg `0.3431` n `150`; fx avg `0.02` n `6`; index avg `0.0534` n `26`; metal avg `0.0272` n `20`; unknown avg `0.0851` n `1013`
- 4h: commodity avg `-0.0392` n `13`; crypto_alt avg `0.9492` n `235`; crypto_major avg `0.6293` n `8`; equity avg `-0.7914` n `150`; fx avg `0.0285` n `6`; index avg `-0.1155` n `26`; metal avg `0.1038` n `20`; unknown avg `-0.0137` n `1013`
- 24h: commodity avg `0.5857` n `13`; crypto_alt avg `-2.6983` n `235`; crypto_major avg `-3.8302` n `8`; equity avg `-2.7193` n `150`; fx avg `0.0675` n `6`; index avg `-0.3412` n `26`; metal avg `0.0165` n `20`; unknown avg `6.0073` n `983`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
