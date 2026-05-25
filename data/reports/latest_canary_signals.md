# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T20:07:14.729659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.1182` n `228`; crypto_major avg `0.0049` n `8`; equity avg `0.0218` n `67`; fx avg `0.0019` n `6`; index avg `-0.0822` n `23`; metal avg `0.0065` n `18`; unknown avg `-0.1847` n `405`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `0.0386` n `228`; crypto_major avg `-0.0471` n `8`; equity avg `0.0784` n `67`; fx avg `0.0115` n `6`; index avg `0.0655` n `23`; metal avg `0.0126` n `18`; unknown avg `-0.2107` n `405`
- 4h: commodity avg `-0.4098` n `12`; crypto_alt avg `0.1207` n `228`; crypto_major avg `-0.3762` n `8`; equity avg `0.0875` n `67`; fx avg `0.0415` n `6`; index avg `0.1249` n `23`; metal avg `0.1248` n `18`; unknown avg `-0.3247` n `405`
- 24h: commodity avg `-1.0643` n `12`; crypto_alt avg `2.4164` n `228`; crypto_major avg `0.5385` n `8`; equity avg `0.871` n `67`; fx avg `-0.0466` n `6`; index avg `0.6119` n `23`; metal avg `1.685` n `18`; unknown avg `1.3093` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
