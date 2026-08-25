# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T06:22:32.024549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.0283` n `231`; crypto_major avg `0.0679` n `8`; equity avg `0.0895` n `122`; fx avg `0.0282` n `6`; index avg `0.0282` n `25`; metal avg `0.0394` n `20`; unknown avg `0.0038` n `794`
- 1h: commodity avg `-0.158` n `12`; crypto_alt avg `-0.1033` n `231`; crypto_major avg `-0.0353` n `8`; equity avg `0.1564` n `122`; fx avg `0.0241` n `6`; index avg `0.0471` n `25`; metal avg `0.0174` n `20`; unknown avg `-0.1128` n `778`
- 4h: commodity avg `-0.3526` n `12`; crypto_alt avg `0.3295` n `231`; crypto_major avg `0.2903` n `8`; equity avg `0.9705` n `122`; fx avg `0.0185` n `6`; index avg `0.1806` n `25`; metal avg `-0.0868` n `20`; unknown avg `-0.084` n `778`
- 24h: commodity avg `-0.1808` n `12`; crypto_alt avg `1.9105` n `231`; crypto_major avg `2.8581` n `8`; equity avg `0.4288` n `122`; fx avg `0.0423` n `6`; index avg `0.0652` n `25`; metal avg `-0.1519` n `20`; unknown avg `0.5175` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
