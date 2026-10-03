# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T11:52:27.103263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `13`; crypto_alt avg `-0.0052` n `235`; crypto_major avg `0.0282` n `8`; equity avg `0.0017` n `143`; fx avg `-0.0016` n `6`; index avg `-0.0011` n `26`; metal avg `0.0027` n `20`; unknown avg `0.1353` n `982`
- 1h: commodity avg `-0.0117` n `13`; crypto_alt avg `0.0575` n `235`; crypto_major avg `0.043` n `8`; equity avg `-0.0117` n `143`; fx avg `-0.0041` n `6`; index avg `-0.0175` n `26`; metal avg `0.0082` n `20`; unknown avg `0.1177` n `980`
- 4h: commodity avg `0.0172` n `13`; crypto_alt avg `0.6736` n `235`; crypto_major avg `0.0962` n `8`; equity avg `0.0326` n `143`; fx avg `-0.0153` n `6`; index avg `-0.0126` n `26`; metal avg `0.0066` n `20`; unknown avg `1.2071` n `964`
- 24h: commodity avg `0.6507` n `13`; crypto_alt avg `-1.7187` n `235`; crypto_major avg `-2.3414` n `8`; equity avg `0.3788` n `142`; fx avg `0.0474` n `6`; index avg `0.1337` n `26`; metal avg `-0.2721` n `20`; unknown avg `-0.3403` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
