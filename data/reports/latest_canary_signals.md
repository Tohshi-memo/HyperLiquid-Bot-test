# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T06:33:09.775945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.04` n `12`; crypto_alt avg `0.135` n `230`; crypto_major avg `0.143` n `8`; equity avg `0.0079` n `93`; fx avg `0.012` n `6`; index avg `0.0073` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.0129` n `767`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.4073` n `230`; crypto_major avg `0.6085` n `8`; equity avg `0.1863` n `93`; fx avg `-0.0062` n `6`; index avg `0.0095` n `25`; metal avg `-0.0084` n `20`; unknown avg `0.0137` n `749`
- 4h: commodity avg `-0.127` n `12`; crypto_alt avg `0.4791` n `230`; crypto_major avg `1.1646` n `8`; equity avg `0.2872` n `93`; fx avg `0.0102` n `6`; index avg `0.0088` n `25`; metal avg `-0.1021` n `20`; unknown avg `0.1543` n `749`
- 24h: commodity avg `-0.015` n `12`; crypto_alt avg `1.7666` n `230`; crypto_major avg `3.6388` n `8`; equity avg `1.6968` n `92`; fx avg `0.0704` n `6`; index avg `0.5014` n `25`; metal avg `0.1923` n `20`; unknown avg `0.3222` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
