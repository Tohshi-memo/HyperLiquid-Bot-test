# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T23:52:26.237266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1022` n `12`; crypto_alt avg `-0.0026` n `234`; crypto_major avg `-0.0746` n `8`; equity avg `0.0175` n `140`; fx avg `0.0106` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0133` n `20`; unknown avg `1.7203` n `942`
- 1h: commodity avg `0.1814` n `12`; crypto_alt avg `0.104` n `234`; crypto_major avg `-0.2515` n `8`; equity avg `0.0326` n `140`; fx avg `0.0216` n `6`; index avg `0.0082` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.331` n `940`
- 4h: commodity avg `0.1671` n `12`; crypto_alt avg `0.3696` n `234`; crypto_major avg `-0.5793` n `8`; equity avg `0.166` n `140`; fx avg `0.0472` n `6`; index avg `0.0229` n `26`; metal avg `-0.0224` n `20`; unknown avg `0.5142` n `872`
- 24h: commodity avg `0.1038` n `12`; crypto_alt avg `6.4364` n `234`; crypto_major avg `6.2653` n `8`; equity avg `1.3128` n `140`; fx avg `0.2389` n `6`; index avg `0.066` n `26`; metal avg `0.317` n `20`; unknown avg `3.8432` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
