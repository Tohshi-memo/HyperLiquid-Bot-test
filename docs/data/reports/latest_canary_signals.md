# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T10:07:29.534811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0389` n `12`; crypto_alt avg `0.1622` n `230`; crypto_major avg `0.1743` n `8`; equity avg `-0.0184` n `93`; fx avg `0.0032` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0341` n `767`
- 1h: commodity avg `0.1846` n `12`; crypto_alt avg `0.0953` n `230`; crypto_major avg `0.056` n `8`; equity avg `-0.0515` n `93`; fx avg `0.0069` n `6`; index avg `-0.0266` n `25`; metal avg `-0.1045` n `20`; unknown avg `-0.0615` n `767`
- 4h: commodity avg `0.0983` n `12`; crypto_alt avg `-0.1756` n `230`; crypto_major avg `-0.2078` n `8`; equity avg `-0.3448` n `93`; fx avg `0.0194` n `6`; index avg `-0.1145` n `25`; metal avg `-0.0461` n `20`; unknown avg `-0.1863` n `765`
- 24h: commodity avg `-0.1224` n `12`; crypto_alt avg `1.7309` n `230`; crypto_major avg `3.2594` n `8`; equity avg `1.0741` n `92`; fx avg `0.0298` n `6`; index avg `0.3996` n `25`; metal avg `0.244` n `20`; unknown avg `0.2851` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
