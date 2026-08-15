# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T15:52:24.236296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `0.0525` n `230`; crypto_major avg `0.0121` n `8`; equity avg `-0.0172` n `114`; fx avg `-0.0007` n `6`; index avg `0.0011` n `25`; metal avg `0.0025` n `20`; unknown avg `0.0054` n `791`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `0.2246` n `230`; crypto_major avg `0.1434` n `8`; equity avg `0.0172` n `114`; fx avg `-0.0013` n `6`; index avg `0.0071` n `25`; metal avg `0.0023` n `20`; unknown avg `5.6147` n `791`
- 4h: commodity avg `-0.0361` n `12`; crypto_alt avg `0.4248` n `230`; crypto_major avg `0.2789` n `8`; equity avg `0.0398` n `114`; fx avg `-0.0061` n `6`; index avg `0.0239` n `25`; metal avg `-0.0077` n `20`; unknown avg `-0.0322` n `791`
- 24h: commodity avg `-0.085` n `12`; crypto_alt avg `1.2865` n `230`; crypto_major avg `0.3377` n `8`; equity avg `0.4395` n `114`; fx avg `0.0205` n `6`; index avg `0.0628` n `25`; metal avg `-0.012` n `20`; unknown avg `-0.049` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
