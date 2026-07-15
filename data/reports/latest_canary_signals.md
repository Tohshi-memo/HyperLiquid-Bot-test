# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T16:52:28.955684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0358` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.031` n `12`; crypto_alt avg `0.3031` n `230`; crypto_major avg `0.383` n `8`; equity avg `0.5866` n `94`; fx avg `0.0158` n `6`; index avg `0.0837` n `25`; metal avg `0.0857` n `20`; unknown avg `0.0578` n `768`
- 1h: commodity avg `0.1775` n `12`; crypto_alt avg `-0.6184` n `230`; crypto_major avg `-0.8149` n `8`; equity avg `-0.4733` n `94`; fx avg `0.0355` n `6`; index avg `-0.0905` n `25`; metal avg `-0.157` n `20`; unknown avg `0.5404` n `768`
- 4h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.796` n `230`; crypto_major avg `-0.5442` n `8`; equity avg `-2.58` n `93`; fx avg `0.1079` n `6`; index avg `-0.4631` n `25`; metal avg `-0.3202` n `20`; unknown avg `0.0707` n `768`
- 24h: commodity avg `0.0968` n `12`; crypto_alt avg `-0.1351` n `230`; crypto_major avg `0.6932` n `8`; equity avg `-1.7597` n `92`; fx avg `0.1684` n `6`; index avg `-0.3503` n `25`; metal avg `-0.3071` n `20`; unknown avg `0.2556` n `746`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
