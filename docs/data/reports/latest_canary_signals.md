# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T07:22:25.734577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1196` n `12`; crypto_alt avg `0.2308` n `230`; crypto_major avg `0.159` n `8`; equity avg `0.0166` n `98`; fx avg `0.0172` n `6`; index avg `0.0061` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.1303` n `769`
- 1h: commodity avg `-0.1528` n `12`; crypto_alt avg `0.2266` n `230`; crypto_major avg `-0.0983` n `8`; equity avg `0.0375` n `98`; fx avg `0.0485` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0086` n `20`; unknown avg `-0.1228` n `769`
- 4h: commodity avg `-0.0318` n `12`; crypto_alt avg `-0.5314` n `230`; crypto_major avg `-0.8323` n `8`; equity avg `-0.232` n `98`; fx avg `0.0085` n `6`; index avg `-0.0328` n `25`; metal avg `-0.2038` n `20`; unknown avg `-0.3915` n `753`
- 24h: commodity avg `-0.1021` n `12`; crypto_alt avg `-0.4062` n `230`; crypto_major avg `-0.6757` n `8`; equity avg `-0.1055` n `97`; fx avg `-0.0209` n `6`; index avg `-0.0243` n `25`; metal avg `-0.0291` n `20`; unknown avg `-0.1467` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0891`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0854`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0813`, n `666`, weak_sample_signal
