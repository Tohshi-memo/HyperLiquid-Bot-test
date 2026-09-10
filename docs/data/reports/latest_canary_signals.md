# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T19:52:33.914272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1579` n `233`; crypto_major avg `-0.0913` n `8`; equity avg `-0.1142` n `135`; fx avg `0.0001` n `6`; index avg `0.0045` n `26`; metal avg `-0.0238` n `20`; unknown avg `-0.2148` n `797`
- 1h: commodity avg `0.1574` n `12`; crypto_alt avg `-0.3434` n `233`; crypto_major avg `-0.0879` n `8`; equity avg `-0.3556` n `135`; fx avg `0.0169` n `6`; index avg `-0.0306` n `26`; metal avg `-0.1146` n `20`; unknown avg `9.1409` n `795`
- 4h: commodity avg `0.2992` n `12`; crypto_alt avg `-0.1449` n `233`; crypto_major avg `0.1605` n `8`; equity avg `-0.8468` n `135`; fx avg `0.0106` n `6`; index avg `-0.0742` n `26`; metal avg `-0.3137` n `20`; unknown avg `-0.017` n `788`
- 24h: commodity avg `1.0282` n `12`; crypto_alt avg `-3.3701` n `233`; crypto_major avg `-2.5638` n `8`; equity avg `-2.1522` n `135`; fx avg `0.1138` n `6`; index avg `-0.3248` n `26`; metal avg `-1.2678` n `20`; unknown avg `-0.4857` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
