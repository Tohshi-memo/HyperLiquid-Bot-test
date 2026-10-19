# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T07:37:31.552363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `13`; crypto_alt avg `0.2502` n `237`; crypto_major avg `0.1243` n `8`; equity avg `0.1146` n `151`; fx avg `0.0027` n `6`; index avg `0.0099` n `26`; metal avg `-0.0141` n `20`; unknown avg `1.028` n `1195`
- 1h: commodity avg `-0.0496` n `13`; crypto_alt avg `0.3265` n `237`; crypto_major avg `0.1604` n `8`; equity avg `-0.0837` n `151`; fx avg `-0.011` n `6`; index avg `-0.0349` n `26`; metal avg `0.0311` n `20`; unknown avg `0.5253` n `1190`
- 4h: commodity avg `-0.0512` n `13`; crypto_alt avg `0.492` n `237`; crypto_major avg `0.425` n `8`; equity avg `0.1348` n `151`; fx avg `-0.0483` n `6`; index avg `0.0119` n `26`; metal avg `-0.0237` n `20`; unknown avg `3.9573` n `1162`
- 24h: commodity avg `-0.5101` n `13`; crypto_alt avg `0.9255` n `237`; crypto_major avg `1.4996` n `8`; equity avg `2.8539` n `151`; fx avg `-0.051` n `6`; index avg `0.5056` n `26`; metal avg `0.3108` n `20`; unknown avg `2.9071` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1936`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0638`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0589`, n `666`, weak_sample_signal
