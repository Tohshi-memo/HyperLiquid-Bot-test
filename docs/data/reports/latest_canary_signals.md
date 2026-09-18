# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T21:37:32.964569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.0702` n `234`; crypto_major avg `0.0932` n `8`; equity avg `-0.0157` n `140`; fx avg `-0.0014` n `6`; index avg `0.002` n `26`; metal avg `0.0173` n `20`; unknown avg `25.0339` n `934`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `0.3096` n `234`; crypto_major avg `0.2016` n `8`; equity avg `0.04` n `140`; fx avg `0.034` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0178` n `20`; unknown avg `10.0033` n `932`
- 4h: commodity avg `-0.0792` n `12`; crypto_alt avg `1.3527` n `234`; crypto_major avg `0.9157` n `8`; equity avg `0.6695` n `140`; fx avg `0.0636` n `6`; index avg `0.1428` n `26`; metal avg `-0.095` n `20`; unknown avg `3.4515` n `888`
- 24h: commodity avg `-0.0857` n `12`; crypto_alt avg `7.1516` n `234`; crypto_major avg `7.0178` n `8`; equity avg `1.2729` n `140`; fx avg `0.2622` n `6`; index avg `0.0429` n `26`; metal avg `0.3917` n `20`; unknown avg `4.951` n `727`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
