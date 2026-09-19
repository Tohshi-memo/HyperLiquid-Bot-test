# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T07:22:30.321351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.0157` n `234`; crypto_major avg `-0.0019` n `8`; equity avg `0.0173` n `140`; fx avg `-0.0047` n `6`; index avg `0.0308` n `26`; metal avg `0.0064` n `20`; unknown avg `-0.0268` n `942`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.5018` n `234`; crypto_major avg `0.1762` n `8`; equity avg `0.043` n `140`; fx avg `0.0049` n `6`; index avg `0.0359` n `26`; metal avg `0.0078` n `20`; unknown avg `0.1556` n `940`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.9468` n `234`; crypto_major avg `-0.3506` n `8`; equity avg `-0.0733` n `140`; fx avg `0.0106` n `6`; index avg `0.0311` n `26`; metal avg `-0.0118` n `20`; unknown avg `0.0765` n `894`
- 24h: commodity avg `0.3414` n `12`; crypto_alt avg `3.0583` n `234`; crypto_major avg `3.9899` n `8`; equity avg `0.0731` n `140`; fx avg `0.08` n `6`; index avg `-0.0598` n `26`; metal avg `-0.1987` n `20`; unknown avg `2.1761` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
