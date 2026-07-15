# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T06:37:29.095365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0286` n `12`; crypto_alt avg `0.0816` n `230`; crypto_major avg `0.0444` n `8`; equity avg `0.0082` n `93`; fx avg `-0.0006` n `6`; index avg `0.0107` n `25`; metal avg `0.0394` n `20`; unknown avg `-0.1028` n `767`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `0.3535` n `230`; crypto_major avg `0.5092` n `8`; equity avg `0.1866` n `93`; fx avg `-0.0188` n `6`; index avg `0.013` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0395` n `749`
- 4h: commodity avg `-0.1383` n `12`; crypto_alt avg `0.4252` n `230`; crypto_major avg `1.065` n `8`; equity avg `0.286` n `93`; fx avg `-0.0024` n `6`; index avg `0.0123` n `25`; metal avg `-0.0898` n `20`; unknown avg `0.1008` n `749`
- 24h: commodity avg `-0.0263` n `12`; crypto_alt avg `1.7111` n `230`; crypto_major avg `3.5363` n `8`; equity avg `1.7065` n `92`; fx avg `0.0578` n `6`; index avg `0.5048` n `25`; metal avg `0.2047` n `20`; unknown avg `0.2669` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
