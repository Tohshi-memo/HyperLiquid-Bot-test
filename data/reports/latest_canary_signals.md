# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T02:22:25.405880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.1662` n `230`; crypto_major avg `-0.1239` n `8`; equity avg `-0.0477` n `96`; fx avg `-0.0002` n `6`; index avg `0.0041` n `25`; metal avg `0.0078` n `20`; unknown avg `0.4402` n `770`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.0821` n `230`; crypto_major avg `0.2308` n `8`; equity avg `0.136` n `96`; fx avg `0.0141` n `6`; index avg `0.0019` n `25`; metal avg `0.0318` n `20`; unknown avg `0.4017` n `770`
- 4h: commodity avg `-0.0546` n `12`; crypto_alt avg `0.1572` n `230`; crypto_major avg `0.3724` n `8`; equity avg `0.2165` n `96`; fx avg `0.0535` n `6`; index avg `-0.0179` n `25`; metal avg `0.0588` n `20`; unknown avg `-0.5519` n `770`
- 24h: commodity avg `0.272` n `12`; crypto_alt avg `-0.0988` n `230`; crypto_major avg `0.7735` n `8`; equity avg `-0.2038` n `96`; fx avg `-0.0108` n `6`; index avg `-0.0166` n `25`; metal avg `-0.003` n `20`; unknown avg `0.0564` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
