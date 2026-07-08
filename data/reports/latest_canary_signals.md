# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T10:52:30.623459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.0083` n `229`; crypto_major avg `-0.0153` n `8`; equity avg `0.0506` n `91`; fx avg `0.0034` n `6`; index avg `0.0078` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.0112` n `763`
- 1h: commodity avg `-0.2102` n `12`; crypto_alt avg `0.0834` n `229`; crypto_major avg `0.128` n `8`; equity avg `0.4272` n `91`; fx avg `-0.0134` n `6`; index avg `0.0725` n `25`; metal avg `0.0178` n `20`; unknown avg `0.0122` n `763`
- 4h: commodity avg `0.3458` n `12`; crypto_alt avg `-1.0354` n `229`; crypto_major avg `-0.6319` n `8`; equity avg `-1.274` n `91`; fx avg `0.0533` n `6`; index avg `-0.3038` n `25`; metal avg `-1.1304` n `20`; unknown avg `-0.2487` n `763`
- 24h: commodity avg `1.1436` n `12`; crypto_alt avg `-3.8335` n `229`; crypto_major avg `-2.8855` n `8`; equity avg `-2.7529` n `91`; fx avg `-0.1119` n `6`; index avg `-0.5846` n `25`; metal avg `-1.2293` n `20`; unknown avg `-0.8028` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
