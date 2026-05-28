# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T18:52:22.963579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0512` n `12`; crypto_alt avg `0.1975` n `228`; crypto_major avg `0.2806` n `8`; equity avg `0.0917` n `69`; fx avg `-0.0063` n `6`; index avg `-0.0087` n `23`; metal avg `-0.0154` n `18`; unknown avg `0.0022` n `417`
- 1h: commodity avg `0.3271` n `12`; crypto_alt avg `0.4252` n `228`; crypto_major avg `0.5489` n `8`; equity avg `0.2665` n `69`; fx avg `0.0043` n `6`; index avg `-0.0668` n `23`; metal avg `-0.1572` n `18`; unknown avg `0.261` n `417`
- 4h: commodity avg `0.2916` n `12`; crypto_alt avg `2.176` n `228`; crypto_major avg `2.213` n `8`; equity avg `1.2719` n `69`; fx avg `-0.0065` n `6`; index avg `0.8318` n `23`; metal avg `0.811` n `18`; unknown avg `0.4918` n `417`
- 24h: commodity avg `1.2438` n `12`; crypto_alt avg `-3.0889` n `228`; crypto_major avg `-0.5688` n `8`; equity avg `1.6524` n `69`; fx avg `-0.0206` n `6`; index avg `0.8871` n `23`; metal avg `0.5901` n `18`; unknown avg `-0.7306` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
