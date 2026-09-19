# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T05:07:26.277402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `0.2995` n `234`; crypto_major avg `0.2839` n `8`; equity avg `0.0285` n `140`; fx avg `0.0087` n `6`; index avg `-0.0068` n `26`; metal avg `0.0002` n `20`; unknown avg `-0.1266` n `940`
- 1h: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.5634` n `234`; crypto_major avg `-0.2187` n `8`; equity avg `-0.0466` n `140`; fx avg `-0.0016` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0104` n `20`; unknown avg `-0.0873` n `940`
- 4h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.1621` n `234`; crypto_major avg `-0.1648` n `8`; equity avg `-0.1617` n `140`; fx avg `0.014` n `6`; index avg `-0.0292` n `26`; metal avg `0.0024` n `20`; unknown avg `0.5338` n `914`
- 24h: commodity avg `0.1027` n `12`; crypto_alt avg `3.7926` n `234`; crypto_major avg `4.5637` n `8`; equity avg `0.5249` n `140`; fx avg `0.0136` n `6`; index avg `0.0029` n `26`; metal avg `0.0246` n `20`; unknown avg `2.3892` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
