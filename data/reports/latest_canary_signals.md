# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T16:22:29.980342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `0.06` n `236`; crypto_major avg `-0.0277` n `8`; equity avg `0.0453` n `151`; fx avg `-0.0128` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0017` n `20`; unknown avg `1.8845` n `1193`
- 1h: commodity avg `-0.0254` n `13`; crypto_alt avg `-0.4639` n `236`; crypto_major avg `-0.4125` n `8`; equity avg `-0.1264` n `151`; fx avg `-0.034` n `6`; index avg `-0.0384` n `26`; metal avg `-0.0211` n `20`; unknown avg `-0.294` n `1185`
- 4h: commodity avg `0.0661` n `13`; crypto_alt avg `-1.0339` n `236`; crypto_major avg `-0.5477` n `8`; equity avg `-0.2633` n `151`; fx avg `-0.0506` n `6`; index avg `-0.0508` n `26`; metal avg `-0.0376` n `20`; unknown avg `1.6645` n `1167`
- 24h: commodity avg `0.3488` n `13`; crypto_alt avg `-2.4471` n `236`; crypto_major avg `-1.0146` n `8`; equity avg `-1.5365` n `151`; fx avg `-0.0158` n `6`; index avg `-0.3138` n `26`; metal avg `-0.1018` n `20`; unknown avg `3.4677` n `1056`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.171`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1469`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
