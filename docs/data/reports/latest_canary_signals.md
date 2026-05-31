# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T11:37:21.993987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `0.1511` n `228`; crypto_major avg `0.0475` n `8`; equity avg `0.0177` n `69`; fx avg `0.0157` n `6`; index avg `-0.0462` n `23`; metal avg `0.0036` n `18`; unknown avg `0.1304` n `421`
- 1h: commodity avg `0.1513` n `12`; crypto_alt avg `0.3782` n `228`; crypto_major avg `0.0218` n `8`; equity avg `0.0453` n `69`; fx avg `-0.0209` n `6`; index avg `-0.0571` n `23`; metal avg `-0.0055` n `18`; unknown avg `0.1714` n `421`
- 4h: commodity avg `0.1514` n `12`; crypto_alt avg `0.3252` n `228`; crypto_major avg `-0.1084` n `8`; equity avg `-0.0522` n `69`; fx avg `-0.0388` n `6`; index avg `-0.1241` n `23`; metal avg `-0.0233` n `18`; unknown avg `-0.0867` n `421`
- 24h: commodity avg `0.2851` n `12`; crypto_alt avg `0.1511` n `228`; crypto_major avg `1.0948` n `8`; equity avg `1.1317` n `69`; fx avg `0.0` n `6`; index avg `-0.1339` n `23`; metal avg `-0.0804` n `18`; unknown avg `0.4009` n `401`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
