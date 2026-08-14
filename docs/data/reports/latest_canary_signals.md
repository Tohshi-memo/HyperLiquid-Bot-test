# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T03:22:28.234055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0372` n `230`; crypto_major avg `0.1038` n `8`; equity avg `0.1141` n `113`; fx avg `-0.0039` n `6`; index avg `0.025` n `25`; metal avg `0.022` n `20`; unknown avg `0.0549` n `787`
- 1h: commodity avg `0.0543` n `12`; crypto_alt avg `-0.1709` n `230`; crypto_major avg `-0.0532` n `8`; equity avg `0.0239` n `113`; fx avg `-0.0233` n `6`; index avg `-0.0014` n `25`; metal avg `0.0931` n `20`; unknown avg `-0.2384` n `787`
- 4h: commodity avg `0.0247` n `12`; crypto_alt avg `-0.0935` n `230`; crypto_major avg `-0.026` n `8`; equity avg `-0.3495` n `113`; fx avg `-0.0658` n `6`; index avg `-0.0535` n `25`; metal avg `-0.1619` n `20`; unknown avg `0.2648` n `787`
- 24h: commodity avg `-0.3137` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `0.0688` n `8`; equity avg `0.8196` n `113`; fx avg `-0.0203` n `6`; index avg `0.2128` n `25`; metal avg `-0.5538` n `20`; unknown avg `0.9664` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2435`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
