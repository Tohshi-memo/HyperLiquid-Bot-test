# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T02:37:25.182147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `13`; crypto_alt avg `-0.1961` n `235`; crypto_major avg `-0.0835` n `8`; equity avg `-0.026` n `150`; fx avg `-0.0009` n `6`; index avg `0.0008` n `26`; metal avg `0.0158` n `20`; unknown avg `0.129` n `1078`
- 1h: commodity avg `-0.1153` n `13`; crypto_alt avg `-0.0396` n `235`; crypto_major avg `0.1169` n `8`; equity avg `0.1718` n `150`; fx avg `0.0094` n `6`; index avg `0.0458` n `26`; metal avg `0.0592` n `20`; unknown avg `0.594` n `1076`
- 4h: commodity avg `-0.0763` n `13`; crypto_alt avg `0.1725` n `235`; crypto_major avg `0.018` n `8`; equity avg `0.2112` n `150`; fx avg `0.0358` n `6`; index avg `0.0478` n `26`; metal avg `0.3856` n `20`; unknown avg `0.8447` n `1069`
- 24h: commodity avg `0.202` n `13`; crypto_alt avg `-3.2154` n `235`; crypto_major avg `-3.5175` n `8`; equity avg `-2.3666` n `150`; fx avg `0.1079` n `6`; index avg `-0.2728` n `26`; metal avg `0.0307` n `20`; unknown avg `6.8043` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
