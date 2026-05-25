# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T15:52:17.023255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.044` n `12`; crypto_alt avg `-0.0483` n `228`; crypto_major avg `-0.1012` n `8`; equity avg `-0.0324` n `67`; fx avg `-0.0117` n `6`; index avg `0.1074` n `23`; metal avg `0.0424` n `18`; unknown avg `-0.1373` n `405`
- 1h: commodity avg `-0.1113` n `12`; crypto_alt avg `-0.0438` n `228`; crypto_major avg `-0.1705` n `8`; equity avg `-0.0298` n `67`; fx avg `-0.0134` n `6`; index avg `0.1209` n `23`; metal avg `0.2548` n `18`; unknown avg `0.743` n `405`
- 4h: commodity avg `0.2078` n `12`; crypto_alt avg `0.7361` n `228`; crypto_major avg `0.1233` n `8`; equity avg `0.035` n `67`; fx avg `-0.0187` n `6`; index avg `0.1569` n `23`; metal avg `0.2437` n `18`; unknown avg `0.9039` n `405`
- 24h: commodity avg `-0.731` n `12`; crypto_alt avg `1.9779` n `228`; crypto_major avg `0.7564` n `8`; equity avg `1.0244` n `67`; fx avg `-0.0058` n `6`; index avg `0.5747` n `23`; metal avg `1.4644` n `18`; unknown avg `1.8266` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
