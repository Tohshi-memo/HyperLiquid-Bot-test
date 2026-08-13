# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T19:37:30.638926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.0083` n `230`; crypto_major avg `0.0305` n `8`; equity avg `-0.1574` n `113`; fx avg `0.0046` n `6`; index avg `-0.0239` n `25`; metal avg `0.0207` n `20`; unknown avg `0.0099` n `787`
- 1h: commodity avg `0.0277` n `12`; crypto_alt avg `0.236` n `230`; crypto_major avg `0.3936` n `8`; equity avg `-0.0664` n `113`; fx avg `0.0077` n `6`; index avg `-0.0151` n `25`; metal avg `-0.1012` n `20`; unknown avg `0.2759` n `787`
- 4h: commodity avg `-0.2332` n `12`; crypto_alt avg `-0.576` n `230`; crypto_major avg `-0.0267` n `8`; equity avg `0.0014` n `113`; fx avg `0.0028` n `6`; index avg `0.0384` n `25`; metal avg `-0.0948` n `20`; unknown avg `-0.0934` n `787`
- 24h: commodity avg `-0.4911` n `12`; crypto_alt avg `-0.2328` n `230`; crypto_major avg `0.3643` n `8`; equity avg `1.3607` n `113`; fx avg `0.017` n `6`; index avg `0.3133` n `25`; metal avg `-0.5286` n `20`; unknown avg `0.0587` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2339`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
