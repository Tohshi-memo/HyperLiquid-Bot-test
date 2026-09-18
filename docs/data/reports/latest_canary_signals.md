# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T23:37:29.733770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.069` n `12`; crypto_alt avg `-0.1267` n `234`; crypto_major avg `-0.2303` n `8`; equity avg `-0.0068` n `140`; fx avg `-0.0116` n `6`; index avg `0.0052` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.3441` n `942`
- 1h: commodity avg `0.0831` n `12`; crypto_alt avg `0.1785` n `234`; crypto_major avg `-0.1986` n `8`; equity avg `-0.0144` n `140`; fx avg `0.0102` n `6`; index avg `0.0034` n `26`; metal avg `0.0005` n `20`; unknown avg `5.417` n `940`
- 4h: commodity avg `0.0734` n `12`; crypto_alt avg `0.4951` n `234`; crypto_major avg `-0.2882` n `8`; equity avg `0.3114` n `140`; fx avg `0.0399` n `6`; index avg `0.0636` n `26`; metal avg `-0.0225` n `20`; unknown avg `0.428` n `872`
- 24h: commodity avg `0.0146` n `12`; crypto_alt avg `6.5401` n `234`; crypto_major avg `6.4397` n `8`; equity avg `1.3027` n `140`; fx avg `0.2347` n `6`; index avg `0.0588` n `26`; metal avg `0.3422` n `20`; unknown avg `4.0065` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
