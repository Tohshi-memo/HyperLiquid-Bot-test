# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T16:36:09.801825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0611` n `12`; crypto_alt avg `0.1301` n `228`; crypto_major avg `0.0339` n `8`; equity avg `0.0081` n `67`; fx avg `0.0018` n `6`; index avg `-0.0298` n `23`; metal avg `0.0232` n `18`; unknown avg `-0.2251` n `405`
- 1h: commodity avg `0.0595` n `12`; crypto_alt avg `0.1526` n `228`; crypto_major avg `-0.1795` n `8`; equity avg `-0.0964` n `67`; fx avg `-0.0127` n `6`; index avg `0.014` n `23`; metal avg `0.046` n `18`; unknown avg `-0.3044` n `405`
- 4h: commodity avg `-0.1591` n `12`; crypto_alt avg `0.7695` n `228`; crypto_major avg `-0.1229` n `8`; equity avg `-0.0043` n `67`; fx avg `-0.0168` n `6`; index avg `0.0353` n `23`; metal avg `0.396` n `18`; unknown avg `0.1956` n `405`
- 24h: commodity avg `-0.7923` n `12`; crypto_alt avg `2.3299` n `228`; crypto_major avg `0.7127` n `8`; equity avg `0.8904` n `67`; fx avg `-0.0305` n `6`; index avg `0.4867` n `23`; metal avg `1.44` n `18`; unknown avg `1.04` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
