# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T17:22:37.565541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.43` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7637` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `0.3863` n `237`; crypto_major avg `0.2287` n `8`; equity avg `0.2233` n `151`; fx avg `0.0135` n `6`; index avg `0.0564` n `26`; metal avg `0.0837` n `20`; unknown avg `0.8743` n `1233`
- 1h: commodity avg `0.0599` n `13`; crypto_alt avg `-0.15` n `237`; crypto_major avg `-0.5884` n `8`; equity avg `-0.8072` n `151`; fx avg `0.011` n `6`; index avg `-0.0989` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.3561` n `1231`
- 4h: commodity avg `-0.137` n `13`; crypto_alt avg `-0.7288` n `237`; crypto_major avg `-0.6012` n `8`; equity avg `-2.3649` n `151`; fx avg `0.032` n `6`; index avg `-0.1656` n `26`; metal avg `-0.2037` n `20`; unknown avg `0.5319` n `1083`
- 24h: commodity avg `0.484` n `13`; crypto_alt avg `-4.914` n `237`; crypto_major avg `-3.9201` n `8`; equity avg `-5.0441` n `151`; fx avg `-0.1247` n `6`; index avg `-0.607` n `26`; metal avg `-0.91` n `20`; unknown avg `3.3935` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
