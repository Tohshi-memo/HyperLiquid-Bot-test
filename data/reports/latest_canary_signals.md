# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T11:37:27.485666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.1388` n `230`; crypto_major avg `-0.1733` n `8`; equity avg `-0.0483` n `100`; fx avg `-0.003` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0191` n `20`; unknown avg `-0.0194` n `773`
- 1h: commodity avg `-0.067` n `12`; crypto_alt avg `-0.1869` n `230`; crypto_major avg `-0.255` n `8`; equity avg `-0.1068` n `100`; fx avg `-0.0032` n `6`; index avg `0.001` n `25`; metal avg `-0.0288` n `20`; unknown avg `-0.1128` n `773`
- 4h: commodity avg `-0.1388` n `12`; crypto_alt avg `-0.7008` n `230`; crypto_major avg `-0.6558` n `8`; equity avg `-0.0272` n `100`; fx avg `-0.0713` n `6`; index avg `0.0272` n `25`; metal avg `0.0821` n `20`; unknown avg `0.0483` n `772`
- 24h: commodity avg `-0.3119` n `12`; crypto_alt avg `-1.4565` n `230`; crypto_major avg `-1.9351` n `8`; equity avg `-1.3079` n `99`; fx avg `-0.125` n `6`; index avg `-0.3516` n `25`; metal avg `-0.2362` n `20`; unknown avg `0.1812` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1007`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0898`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
