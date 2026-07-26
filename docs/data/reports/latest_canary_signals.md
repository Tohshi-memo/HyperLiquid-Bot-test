# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T22:37:25.566938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0313` n `12`; crypto_alt avg `0.1869` n `230`; crypto_major avg `0.2931` n `8`; equity avg `0.0675` n `100`; fx avg `-0.0002` n `6`; index avg `0.0081` n `25`; metal avg `0.0322` n `20`; unknown avg `-0.1104` n `775`
- 1h: commodity avg `-0.4061` n `12`; crypto_alt avg `0.7121` n `230`; crypto_major avg `0.826` n `8`; equity avg `0.4477` n `100`; fx avg `0.0018` n `6`; index avg `0.127` n `25`; metal avg `0.1696` n `20`; unknown avg `-0.0116` n `775`
- 4h: commodity avg `-0.375` n `12`; crypto_alt avg `0.8758` n `230`; crypto_major avg `0.9913` n `8`; equity avg `0.4601` n `100`; fx avg `0.0263` n `6`; index avg `0.1035` n `25`; metal avg `0.2249` n `20`; unknown avg `-0.1664` n `775`
- 24h: commodity avg `-0.6011` n `12`; crypto_alt avg `1.6431` n `230`; crypto_major avg `1.8713` n `8`; equity avg `1.093` n `100`; fx avg `0.0484` n `6`; index avg `0.2175` n `25`; metal avg `0.4168` n `20`; unknown avg `0.0992` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
