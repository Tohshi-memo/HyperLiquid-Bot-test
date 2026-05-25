# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T21:07:14.310887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.032` n `228`; crypto_major avg `0.1522` n `8`; equity avg `-0.014` n `67`; fx avg `0.0729` n `6`; index avg `0.036` n `23`; metal avg `0.0195` n `18`; unknown avg `-0.034` n `405`
- 1h: commodity avg `0.0948` n `12`; crypto_alt avg `-0.5139` n `228`; crypto_major avg `-0.2178` n `8`; equity avg `-0.0709` n `67`; fx avg `0.0512` n `6`; index avg `-0.0054` n `23`; metal avg `0.0116` n `18`; unknown avg `-0.386` n `405`
- 4h: commodity avg `0.3536` n `12`; crypto_alt avg `-0.7805` n `228`; crypto_major avg `-0.6154` n `8`; equity avg `-0.011` n `67`; fx avg `0.079` n `6`; index avg `0.1857` n `23`; metal avg `-0.0654` n `18`; unknown avg `-0.2963` n `405`
- 24h: commodity avg `-1.1609` n `12`; crypto_alt avg `2.0255` n `228`; crypto_major avg `0.408` n `8`; equity avg `0.7682` n `67`; fx avg `-0.0104` n `6`; index avg `0.701` n `23`; metal avg `1.8251` n `18`; unknown avg `1.2108` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
