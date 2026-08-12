# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T23:52:27.959205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0521` n `230`; crypto_major avg `0.0049` n `8`; equity avg `-0.0358` n `113`; fx avg `0.0042` n `6`; index avg `-0.0077` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0724` n `786`
- 1h: commodity avg `0.0068` n `12`; crypto_alt avg `0.1523` n `230`; crypto_major avg `0.0674` n `8`; equity avg `0.1033` n `113`; fx avg `0.0009` n `6`; index avg `-0.0078` n `25`; metal avg `0.0507` n `20`; unknown avg `-0.0301` n `786`
- 4h: commodity avg `-0.0619` n `12`; crypto_alt avg `-0.4418` n `230`; crypto_major avg `-0.2009` n `8`; equity avg `-0.0959` n `113`; fx avg `-0.0065` n `6`; index avg `0.0053` n `25`; metal avg `-0.0196` n `20`; unknown avg `-0.1659` n `786`
- 24h: commodity avg `-0.0033` n `12`; crypto_alt avg `-1.3872` n `230`; crypto_major avg `-0.5878` n `8`; equity avg `2.8135` n `113`; fx avg `0.0242` n `6`; index avg `0.3819` n `25`; metal avg `0.1623` n `20`; unknown avg `-0.0688` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
