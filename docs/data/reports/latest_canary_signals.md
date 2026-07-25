# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T02:37:25.319826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.0387` n `230`; crypto_major avg `-0.0229` n `8`; equity avg `0.0443` n `100`; fx avg `-0.0066` n `6`; index avg `0.004` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.1062` n `774`
- 1h: commodity avg `-0.036` n `12`; crypto_alt avg `-0.0795` n `230`; crypto_major avg `-0.0445` n `8`; equity avg `0.0338` n `100`; fx avg `-0.0277` n `6`; index avg `0.0038` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.1731` n `774`
- 4h: commodity avg `-0.0735` n `12`; crypto_alt avg `0.0011` n `230`; crypto_major avg `0.0866` n `8`; equity avg `0.0134` n `100`; fx avg `0.0023` n `6`; index avg `0.0221` n `25`; metal avg `-0.0221` n `20`; unknown avg `-0.218` n `774`
- 24h: commodity avg `-0.3484` n `12`; crypto_alt avg `-0.8399` n `230`; crypto_major avg `-0.6394` n `8`; equity avg `-2.5389` n `100`; fx avg `-0.0447` n `6`; index avg `-0.2088` n `25`; metal avg `0.1406` n `20`; unknown avg `14.0516` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1214`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1145`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1063`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
