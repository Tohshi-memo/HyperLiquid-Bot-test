# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T04:07:30.505458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0673` n `13`; crypto_alt avg `0.0068` n `236`; crypto_major avg `-0.0661` n `8`; equity avg `0.2044` n `151`; fx avg `0.0044` n `6`; index avg `0.0293` n `26`; metal avg `0.0372` n `20`; unknown avg `-0.0579` n `1126`
- 1h: commodity avg `0.0354` n `13`; crypto_alt avg `-0.007` n `236`; crypto_major avg `-0.1605` n `8`; equity avg `0.4922` n `151`; fx avg `0.0234` n `6`; index avg `0.0764` n `26`; metal avg `0.0522` n `20`; unknown avg `0.9464` n `1126`
- 4h: commodity avg `-0.0403` n `13`; crypto_alt avg `-0.3913` n `236`; crypto_major avg `-0.2503` n `8`; equity avg `0.9811` n `151`; fx avg `0.0836` n `6`; index avg `0.176` n `26`; metal avg `0.2919` n `20`; unknown avg `1.1323` n `1126`
- 24h: commodity avg `-0.004` n `13`; crypto_alt avg `3.6173` n `236`; crypto_major avg `2.0398` n `8`; equity avg `2.9352` n `151`; fx avg `0.0347` n `6`; index avg `0.4825` n `26`; metal avg `0.602` n `20`; unknown avg `26.5013` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0995`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0892`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0738`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.068`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
