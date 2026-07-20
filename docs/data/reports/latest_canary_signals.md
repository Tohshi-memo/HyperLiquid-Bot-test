# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T07:49:50.443282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0858` n `12`; crypto_alt avg `0.1195` n `230`; crypto_major avg `0.0737` n `8`; equity avg `-0.0252` n `98`; fx avg `-0.0036` n `6`; index avg `-0.0035` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.0505` n `769`
- 1h: commodity avg `-0.268` n `12`; crypto_alt avg `0.5035` n `230`; crypto_major avg `0.4633` n `8`; equity avg `0.2631` n `98`; fx avg `0.028` n `6`; index avg `0.0672` n `25`; metal avg `0.2146` n `20`; unknown avg `-0.0681` n `769`
- 4h: commodity avg `-0.2758` n `12`; crypto_alt avg `-0.299` n `230`; crypto_major avg `-0.7227` n `8`; equity avg `-0.2062` n `98`; fx avg `0.0066` n `6`; index avg `-0.0401` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.3713` n `753`
- 24h: commodity avg `-0.3618` n `12`; crypto_alt avg `-0.0647` n `230`; crypto_major avg `-0.4767` n `8`; equity avg `0.0719` n `97`; fx avg `-0.0282` n `6`; index avg `0.0327` n `25`; metal avg `0.188` n `20`; unknown avg `-0.1224` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.088`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
