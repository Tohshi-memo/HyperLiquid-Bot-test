# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T20:03:49.137423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `0.1001` n `228`; crypto_major avg `0.0311` n `8`; equity avg `0.0182` n `67`; fx avg `0.0031` n `6`; index avg `-0.1454` n `23`; metal avg `-0.0077` n `18`; unknown avg `-0.1339` n `405`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.0207` n `228`; crypto_major avg `-0.0208` n `8`; equity avg `0.0749` n `67`; fx avg `0.0128` n `6`; index avg `0.0018` n `23`; metal avg `-0.0016` n `18`; unknown avg `-0.1376` n `405`
- 4h: commodity avg `-0.4282` n `12`; crypto_alt avg `0.1026` n `228`; crypto_major avg `-0.3502` n `8`; equity avg `0.0839` n `67`; fx avg `0.0427` n `6`; index avg `0.0615` n `23`; metal avg `0.1105` n `18`; unknown avg `-0.2144` n `405`
- 24h: commodity avg `-1.0824` n `12`; crypto_alt avg `2.3977` n `228`; crypto_major avg `0.5643` n `8`; equity avg `0.8673` n `67`; fx avg `-0.0453` n `6`; index avg `0.5487` n `23`; metal avg `1.6706` n `18`; unknown avg `1.32` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
