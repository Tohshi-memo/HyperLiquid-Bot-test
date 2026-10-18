# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T07:52:31.614011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `13`; crypto_alt avg `0.0483` n `237`; crypto_major avg `-0.036` n `8`; equity avg `0.0016` n `151`; fx avg `0.006` n `6`; index avg `0.0046` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.0137` n `1193`
- 1h: commodity avg `0.013` n `13`; crypto_alt avg `-0.3202` n `237`; crypto_major avg `-0.1868` n `8`; equity avg `0.0035` n `151`; fx avg `0.0104` n `6`; index avg `0.0133` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0065` n `1189`
- 4h: commodity avg `-0.0398` n `13`; crypto_alt avg `-1.0696` n `237`; crypto_major avg `-0.7111` n `8`; equity avg `-0.0256` n `151`; fx avg `0.0088` n `6`; index avg `0.033` n `26`; metal avg `-0.0165` n `20`; unknown avg `0.1566` n `1167`
- 24h: commodity avg `0.0919` n `13`; crypto_alt avg `-2.7046` n `236`; crypto_major avg `-1.0726` n `8`; equity avg `-0.8047` n `151`; fx avg `-0.0389` n `6`; index avg `-0.0899` n `26`; metal avg `-0.0713` n `20`; unknown avg `3.9762` n `1055`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1717`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1327`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0832`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
