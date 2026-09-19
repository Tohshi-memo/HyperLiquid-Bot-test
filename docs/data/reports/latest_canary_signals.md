# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T00:43:00.451850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.1434` n `234`; crypto_major avg `0.2728` n `8`; equity avg `-0.0167` n `140`; fx avg `0.0097` n `6`; index avg `0.0108` n `26`; metal avg `-0.0133` n `20`; unknown avg `-0.1384` n `942`
- 1h: commodity avg `0.0867` n `12`; crypto_alt avg `0.4647` n `234`; crypto_major avg `0.4989` n `8`; equity avg `0.0457` n `140`; fx avg `-0.0035` n `6`; index avg `0.013` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.1872` n `934`
- 4h: commodity avg `0.1818` n `12`; crypto_alt avg `0.6662` n `234`; crypto_major avg `0.4056` n `8`; equity avg `0.0548` n `140`; fx avg `0.0256` n `6`; index avg `-0.002` n `26`; metal avg `-0.0334` n `20`; unknown avg `10.2832` n `908`
- 24h: commodity avg `0.1545` n `12`; crypto_alt avg `6.8549` n `234`; crypto_major avg `6.9083` n `8`; equity avg `1.4599` n `140`; fx avg `0.1781` n `6`; index avg `0.1244` n `26`; metal avg `0.2338` n `20`; unknown avg `4.1154` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
