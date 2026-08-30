# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T10:07:22.531401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.1991` n `231`; crypto_major avg `0.0914` n `8`; equity avg `0.0102` n `128`; fx avg `0.0048` n `6`; index avg `0.0004` n `26`; metal avg `-0.0053` n `20`; unknown avg `-0.0492` n `793`
- 1h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.1764` n `231`; crypto_major avg `-0.1493` n `8`; equity avg `-0.0238` n `128`; fx avg `0.0019` n `6`; index avg `0.0211` n `26`; metal avg `-0.0097` n `20`; unknown avg `-0.0967` n `793`
- 4h: commodity avg `-0.0029` n `12`; crypto_alt avg `0.0829` n `231`; crypto_major avg `-0.1788` n `8`; equity avg `-0.031` n `128`; fx avg `0.0023` n `6`; index avg `0.0046` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.1289` n `789`
- 24h: commodity avg `-0.0278` n `12`; crypto_alt avg `1.2922` n `231`; crypto_major avg `0.889` n `8`; equity avg `0.2511` n `128`; fx avg `0.0135` n `6`; index avg `0.0794` n `26`; metal avg `0.0761` n `20`; unknown avg `0.6948` n `716`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
