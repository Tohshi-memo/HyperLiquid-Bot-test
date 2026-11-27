# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T07:37:31.478100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `-0.2065` n `239`; crypto_major avg `-0.3107` n `8`; equity avg `-0.2587` n `168`; fx avg `-0.0126` n `6`; index avg `-0.0184` n `27`; metal avg `-0.0131` n `20`; unknown avg `1.7727` n `1263`
- 1h: commodity avg `-0.0691` n `13`; crypto_alt avg `-0.2053` n `239`; crypto_major avg `-0.1291` n `8`; equity avg `-0.6841` n `168`; fx avg `-0.0314` n `6`; index avg `-0.0671` n `27`; metal avg `0.0053` n `20`; unknown avg `0.9832` n `1261`
- 4h: commodity avg `0.0264` n `13`; crypto_alt avg `0.0387` n `239`; crypto_major avg `0.1252` n `8`; equity avg `0.5307` n `168`; fx avg `-0.0422` n `6`; index avg `0.0014` n `27`; metal avg `0.3348` n `20`; unknown avg `64.011` n `1231`
- 24h: commodity avg `0.5024` n `13`; crypto_alt avg `2.0891` n `239`; crypto_major avg `2.5435` n `8`; equity avg `3.3` n `168`; fx avg `-0.0564` n `6`; index avg `0.2556` n `27`; metal avg `1.1817` n `20`; unknown avg `219.247` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
