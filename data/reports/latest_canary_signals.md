# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T21:37:28.871693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0299` n `12`; crypto_alt avg `0.2047` n `230`; crypto_major avg `0.1758` n `8`; equity avg `-0.0098` n `100`; fx avg `-0.0015` n `6`; index avg `0.0065` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0455` n `774`
- 1h: commodity avg `0.0786` n `12`; crypto_alt avg `0.1033` n `230`; crypto_major avg `0.0688` n `8`; equity avg `0.0095` n `100`; fx avg `-0.0036` n `6`; index avg `-0.0044` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.008` n `774`
- 4h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.0644` n `230`; crypto_major avg `-0.1071` n `8`; equity avg `0.1108` n `100`; fx avg `0.0019` n `6`; index avg `0.0266` n `25`; metal avg `0.0144` n `20`; unknown avg `-0.0294` n `774`
- 24h: commodity avg `-0.6186` n `12`; crypto_alt avg `0.5107` n `230`; crypto_major avg `1.2015` n `8`; equity avg `0.3132` n `100`; fx avg `0.0136` n `6`; index avg `0.1287` n `25`; metal avg `0.0157` n `20`; unknown avg `-0.2713` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1216`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1166`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
