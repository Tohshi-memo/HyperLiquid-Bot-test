# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T18:52:24.899640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1116` n `12`; crypto_alt avg `0.1223` n `228`; crypto_major avg `0.0723` n `8`; equity avg `-0.0071` n `74`; fx avg `-0.0027` n `6`; index avg `0.0186` n `23`; metal avg `0.0831` n `18`; unknown avg `-0.0111` n `424`
- 1h: commodity avg `0.3081` n `12`; crypto_alt avg `0.2326` n `228`; crypto_major avg `0.3745` n `8`; equity avg `-0.0632` n `74`; fx avg `-0.0022` n `6`; index avg `0.0413` n `23`; metal avg `0.0273` n `18`; unknown avg `0.1099` n `424`
- 4h: commodity avg `0.2191` n `12`; crypto_alt avg `0.8262` n `228`; crypto_major avg `0.4508` n `8`; equity avg `0.6219` n `74`; fx avg `-0.0381` n `6`; index avg `0.7356` n `23`; metal avg `0.4097` n `18`; unknown avg `1.4214` n `424`
- 24h: commodity avg `-0.6036` n `12`; crypto_alt avg `-5.0505` n `228`; crypto_major avg `-3.665` n `8`; equity avg `-1.0433` n `73`; fx avg `0.1044` n `6`; index avg `0.0551` n `23`; metal avg `0.8106` n `18`; unknown avg `0.3745` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
