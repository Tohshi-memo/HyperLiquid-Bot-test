# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T08:22:24.172514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `13`; crypto_alt avg `0.0033` n `239`; crypto_major avg `-0.0619` n `8`; equity avg `-0.0197` n `158`; fx avg `-0.0004` n `6`; index avg `0.0177` n `27`; metal avg `-0.0018` n `20`; unknown avg `0.0704` n `1262`
- 1h: commodity avg `0.0231` n `13`; crypto_alt avg `-0.0541` n `239`; crypto_major avg `0.0172` n `8`; equity avg `0.0352` n `158`; fx avg `0.0025` n `6`; index avg `0.0342` n `27`; metal avg `0.0079` n `20`; unknown avg `201.6456` n `1240`
- 4h: commodity avg `0.0286` n `13`; crypto_alt avg `-0.1096` n `239`; crypto_major avg `-0.0165` n `8`; equity avg `0.1224` n `158`; fx avg `0.019` n `6`; index avg `0.0398` n `27`; metal avg `0.0074` n `20`; unknown avg `-0.1027` n `1202`
- 24h: commodity avg `0.1552` n `13`; crypto_alt avg `-1.7098` n `239`; crypto_major avg `-0.8055` n `8`; equity avg `-0.0591` n `158`; fx avg `0.07` n `6`; index avg `0.0468` n `27`; metal avg `-0.034` n `20`; unknown avg `158.3817` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
