# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T13:52:36.856216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.515` n `230`; crypto_major avg `-0.5878` n `8`; equity avg `-1.6258` n `102`; fx avg `0.036` n `6`; index avg `-0.2959` n `25`; metal avg `-0.0739` n `20`; unknown avg `-0.2933` n `780`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.3101` n `230`; crypto_major avg `-0.6066` n `8`; equity avg `-1.3207` n `102`; fx avg `-0.1613` n `6`; index avg `-0.1957` n `25`; metal avg `-0.2646` n `20`; unknown avg `-0.0393` n `780`
- 4h: commodity avg `0.1933` n `12`; crypto_alt avg `-0.3061` n `230`; crypto_major avg `-0.4147` n `8`; equity avg `-1.671` n `102`; fx avg `-0.1013` n `6`; index avg `-0.2615` n `25`; metal avg `-0.2978` n `20`; unknown avg `1.0052` n `780`
- 24h: commodity avg `0.4448` n `12`; crypto_alt avg `-1.1169` n `230`; crypto_major avg `-1.1542` n `8`; equity avg `1.7183` n `102`; fx avg `0.0483` n `6`; index avg `0.3842` n `25`; metal avg `-0.4292` n `20`; unknown avg `1.2745` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
