# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T10:52:34.400491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0387` n `12`; crypto_alt avg `0.2828` n `231`; crypto_major avg `0.3509` n `8`; equity avg `0.0219` n `122`; fx avg `0.0086` n `6`; index avg `-0.0011` n `25`; metal avg `0.0015` n `20`; unknown avg `0.068` n `797`
- 1h: commodity avg `0.1017` n `12`; crypto_alt avg `0.8807` n `231`; crypto_major avg `1.1284` n `8`; equity avg `0.0681` n `122`; fx avg `-0.0102` n `6`; index avg `-0.0021` n `25`; metal avg `0.0033` n `20`; unknown avg `0.2351` n `797`
- 4h: commodity avg `0.0117` n `12`; crypto_alt avg `0.195` n `231`; crypto_major avg `0.5387` n `8`; equity avg `-0.0474` n `122`; fx avg `-0.0018` n `6`; index avg `-0.0377` n `25`; metal avg `-0.0418` n `20`; unknown avg `0.1678` n `797`
- 24h: commodity avg `-0.2588` n `12`; crypto_alt avg `-1.4217` n `231`; crypto_major avg `-0.9619` n `8`; equity avg `0.1537` n `122`; fx avg `-0.0236` n `6`; index avg `-0.0455` n `25`; metal avg `0.134` n `20`; unknown avg `0.7213` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
