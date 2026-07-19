# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T15:44:07.788034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.0005` n `230`; crypto_major avg `0.0448` n `8`; equity avg `0.0134` n `96`; fx avg `0.0016` n `6`; index avg `-0.0048` n `25`; metal avg `0.0046` n `20`; unknown avg `0.0023` n `770`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `0.0468` n `230`; crypto_major avg `0.0345` n `8`; equity avg `-0.0509` n `96`; fx avg `0.0016` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0415` n `770`
- 4h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.0562` n `230`; crypto_major avg `-0.038` n `8`; equity avg `-0.0485` n `96`; fx avg `-0.0001` n `6`; index avg `-0.0173` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.0209` n `770`
- 24h: commodity avg `0.2552` n `12`; crypto_alt avg `0.5318` n `230`; crypto_major avg `1.0469` n `8`; equity avg `0.2691` n `96`; fx avg `0.0023` n `6`; index avg `-0.0347` n `25`; metal avg `-0.023` n `20`; unknown avg `0.0899` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1344`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1289`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
