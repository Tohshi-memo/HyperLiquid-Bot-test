# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T19:52:32.845912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `13`; crypto_alt avg `0.1052` n `235`; crypto_major avg `0.1022` n `8`; equity avg `0.0821` n `150`; fx avg `0.0134` n `6`; index avg `0.0109` n `26`; metal avg `0.0104` n `20`; unknown avg `3.7611` n `1077`
- 1h: commodity avg `-0.0585` n `13`; crypto_alt avg `0.8174` n `235`; crypto_major avg `0.6487` n `8`; equity avg `0.1037` n `150`; fx avg `0.0193` n `6`; index avg `0.0131` n `26`; metal avg `0.0217` n `20`; unknown avg `2.667` n `1075`
- 4h: commodity avg `-0.2127` n `13`; crypto_alt avg `0.4436` n `235`; crypto_major avg `0.41` n `8`; equity avg `-0.8813` n `150`; fx avg `0.0036` n `6`; index avg `-0.105` n `26`; metal avg `0.1623` n `20`; unknown avg `1.379` n `1069`
- 24h: commodity avg `0.7051` n `13`; crypto_alt avg `-2.8848` n `235`; crypto_major avg `-3.6572` n `8`; equity avg `-2.9744` n `150`; fx avg `0.0748` n `6`; index avg `-0.3972` n `26`; metal avg `0.0347` n `20`; unknown avg `23.2298` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
