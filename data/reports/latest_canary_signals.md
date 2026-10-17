# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T02:37:27.584493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.3013` n `236`; crypto_major avg `-0.1893` n `8`; equity avg `-0.1021` n `151`; fx avg `0.0017` n `6`; index avg `-0.0055` n `26`; metal avg `0.0155` n `20`; unknown avg `0.2826` n `1193`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `-0.0093` n `236`; crypto_major avg `-0.1172` n `8`; equity avg `-0.0275` n `151`; fx avg `0.0074` n `6`; index avg `0.003` n `26`; metal avg `0.0035` n `20`; unknown avg `-0.2429` n `1189`
- 4h: commodity avg `0.146` n `13`; crypto_alt avg `-0.2654` n `236`; crypto_major avg `-0.4254` n `8`; equity avg `0.1874` n `151`; fx avg `0.0131` n `6`; index avg `0.0123` n `26`; metal avg `-0.0068` n `20`; unknown avg `1.178` n `1183`
- 24h: commodity avg `0.7064` n `13`; crypto_alt avg `-1.5387` n `236`; crypto_major avg `-1.4298` n `8`; equity avg `-4.0346` n `151`; fx avg `-0.0098` n `6`; index avg `-0.6533` n `26`; metal avg `-0.1706` n `20`; unknown avg `40.2453` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1701`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1168`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0769`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
