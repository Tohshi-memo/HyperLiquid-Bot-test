# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T23:07:28.594958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0773` n `12`; crypto_alt avg `0.0938` n `230`; crypto_major avg `0.1065` n `8`; equity avg `0.1126` n `100`; fx avg `-0.0079` n `6`; index avg `0.0359` n `25`; metal avg `-0.0636` n `20`; unknown avg `-0.1109` n `775`
- 1h: commodity avg `0.1298` n `12`; crypto_alt avg `0.318` n `230`; crypto_major avg `0.491` n `8`; equity avg `0.2578` n `100`; fx avg `-0.012` n `6`; index avg `0.0523` n `25`; metal avg `-0.045` n `20`; unknown avg `0.0123` n `775`
- 4h: commodity avg `-0.2709` n `12`; crypto_alt avg `0.95` n `230`; crypto_major avg `1.1431` n `8`; equity avg `0.563` n `100`; fx avg `0.0153` n `6`; index avg `0.1451` n `25`; metal avg `0.1418` n `20`; unknown avg `-0.0951` n `775`
- 24h: commodity avg `-0.4671` n `12`; crypto_alt avg `1.7294` n `230`; crypto_major avg `2.0058` n `8`; equity avg `1.1941` n `100`; fx avg `0.0598` n `6`; index avg `0.2455` n `25`; metal avg `0.3673` n `20`; unknown avg `0.1239` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
