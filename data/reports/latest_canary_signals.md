# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T06:52:31.842431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `-0.0668` n `230`; crypto_major avg `-0.1432` n `8`; equity avg `-0.1685` n `96`; fx avg `-0.0012` n `6`; index avg `-0.0404` n `25`; metal avg `-0.0557` n `20`; unknown avg `0.002` n `768`
- 1h: commodity avg `-0.0482` n `12`; crypto_alt avg `0.3443` n `230`; crypto_major avg `0.2016` n `8`; equity avg `0.2843` n `96`; fx avg `0.0558` n `6`; index avg `0.0126` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0282` n `736`
- 4h: commodity avg `-0.1618` n `12`; crypto_alt avg `0.0367` n `230`; crypto_major avg `-0.5664` n `8`; equity avg `-0.4179` n `94`; fx avg `0.0261` n `6`; index avg `-0.1343` n `25`; metal avg `0.0466` n `20`; unknown avg `-0.0749` n `736`
- 24h: commodity avg `-0.211` n `12`; crypto_alt avg `-2.3125` n `230`; crypto_major avg `-3.9007` n `8`; equity avg `-5.7028` n `94`; fx avg `-0.0506` n `6`; index avg `-0.7866` n `25`; metal avg `-0.7841` n `20`; unknown avg `-0.5918` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
