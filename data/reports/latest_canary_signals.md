# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T07:07:58.073215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0567` n `12`; crypto_alt avg `0.0001` n `230`; crypto_major avg `-0.0482` n `8`; equity avg `0.0086` n `113`; fx avg `-0.0038` n `6`; index avg `0.0023` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.037` n `787`
- 1h: commodity avg `0.0549` n `12`; crypto_alt avg `-0.1986` n `230`; crypto_major avg `-0.3581` n `8`; equity avg `0.0859` n `113`; fx avg `0.0612` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.0445` n `787`
- 4h: commodity avg `0.2508` n `12`; crypto_alt avg `-0.38` n `230`; crypto_major avg `-0.5234` n `8`; equity avg `0.0232` n `113`; fx avg `0.0591` n `6`; index avg `0.0319` n `25`; metal avg `0.0812` n `20`; unknown avg `-0.0357` n `755`
- 24h: commodity avg `-0.1478` n `12`; crypto_alt avg `-0.7119` n `230`; crypto_major avg `-1.0912` n `8`; equity avg `1.317` n `113`; fx avg `-0.0212` n `6`; index avg `0.2845` n `25`; metal avg `-0.2737` n `20`; unknown avg `0.9426` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.221`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
