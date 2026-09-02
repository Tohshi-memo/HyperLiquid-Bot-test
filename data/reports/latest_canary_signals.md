# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T15:07:30.384812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `-0.3159` n `232`; crypto_major avg `-0.3576` n `8`; equity avg `-0.0752` n `133`; fx avg `0.0038` n `6`; index avg `-0.0018` n `26`; metal avg `0.0085` n `20`; unknown avg `-0.292` n `789`
- 1h: commodity avg `0.3084` n `12`; crypto_alt avg `-0.6181` n `232`; crypto_major avg `-0.5939` n `8`; equity avg `-0.1838` n `133`; fx avg `0.0045` n `6`; index avg `0.0256` n `26`; metal avg `-0.0948` n `20`; unknown avg `-0.1203` n `789`
- 4h: commodity avg `0.1468` n `12`; crypto_alt avg `0.282` n `232`; crypto_major avg `0.5462` n `8`; equity avg `1.0053` n `133`; fx avg `-0.1324` n `6`; index avg `0.2524` n `26`; metal avg `0.5756` n `20`; unknown avg `0.6134` n `789`
- 24h: commodity avg `0.7304` n `12`; crypto_alt avg `-1.3211` n `232`; crypto_major avg `-1.5546` n `8`; equity avg `-0.5809` n `132`; fx avg `-0.3483` n `6`; index avg `-0.0659` n `26`; metal avg `0.1772` n `20`; unknown avg `-0.4365` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
