# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T06:52:33.853691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `0.0036` n `230`; crypto_major avg `0.0429` n `8`; equity avg `-0.008` n `100`; fx avg `-0.0015` n `6`; index avg `-0.0002` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0061` n `774`
- 1h: commodity avg `0.0136` n `12`; crypto_alt avg `-0.2892` n `230`; crypto_major avg `-0.0509` n `8`; equity avg `0.0213` n `100`; fx avg `0.0139` n `6`; index avg `0.0145` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0189` n `758`
- 4h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.3149` n `230`; crypto_major avg `-0.1324` n `8`; equity avg `0.094` n `100`; fx avg `0.0054` n `6`; index avg `0.0279` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.1096` n `758`
- 24h: commodity avg `-0.2217` n `12`; crypto_alt avg `-1.8373` n `230`; crypto_major avg `-1.4694` n `8`; equity avg `-2.2691` n `100`; fx avg `-0.0755` n `6`; index avg `-0.1078` n `25`; metal avg `0.125` n `20`; unknown avg `13.5835` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1142`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1023`, n `666`, weak_sample_signal
