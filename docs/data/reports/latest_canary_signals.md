# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T13:07:26.232504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.5662` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1024` n `12`; crypto_alt avg `-0.1771` n `233`; crypto_major avg `-0.2464` n `8`; equity avg `0.0959` n `136`; fx avg `-0.0355` n `6`; index avg `0.0289` n `26`; metal avg `-0.0122` n `20`; unknown avg `5.283` n `794`
- 1h: commodity avg `-0.1192` n `12`; crypto_alt avg `1.8355` n `233`; crypto_major avg `1.8479` n `8`; equity avg `0.8894` n `136`; fx avg `-0.0985` n `6`; index avg `0.1493` n `26`; metal avg `0.2817` n `20`; unknown avg `1.6` n `788`
- 4h: commodity avg `-0.1702` n `12`; crypto_alt avg `0.5802` n `233`; crypto_major avg `1.0231` n `8`; equity avg `0.5144` n `136`; fx avg `-0.1049` n `6`; index avg `0.1247` n `26`; metal avg `0.1664` n `20`; unknown avg `0.7298` n `788`
- 24h: commodity avg `-0.1995` n `12`; crypto_alt avg `0.772` n `233`; crypto_major avg `1.4178` n `8`; equity avg `1.2201` n `136`; fx avg `-0.159` n `6`; index avg `0.2865` n `26`; metal avg `0.1442` n `20`; unknown avg `2.6391` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
