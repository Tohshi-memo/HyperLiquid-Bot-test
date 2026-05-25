# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T13:52:14.177079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0633` n `12`; crypto_alt avg `0.1901` n `228`; crypto_major avg `0.1299` n `8`; equity avg `0.0174` n `67`; fx avg `-0.0008` n `6`; index avg `0.015` n `23`; metal avg `-0.0782` n `18`; unknown avg `0.0416` n `405`
- 1h: commodity avg `0.1524` n `12`; crypto_alt avg `0.1876` n `228`; crypto_major avg `0.0049` n `8`; equity avg `-0.0188` n `67`; fx avg `-0.0138` n `6`; index avg `0.049` n `23`; metal avg `-0.0632` n `18`; unknown avg `0.2505` n `405`
- 4h: commodity avg `0.5362` n `12`; crypto_alt avg `0.2633` n `228`; crypto_major avg `0.019` n `8`; equity avg `0.0043` n `67`; fx avg `0.023` n `6`; index avg `0.109` n `23`; metal avg `-0.1542` n `18`; unknown avg `-0.1081` n `397`
- 24h: commodity avg `0.2216` n `12`; crypto_alt avg `1.1312` n `228`; crypto_major avg `0.095` n `8`; equity avg `0.4728` n `67`; fx avg `-0.0029` n `6`; index avg `0.1979` n `23`; metal avg `0.707` n `18`; unknown avg `0.6025` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
