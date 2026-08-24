# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T16:37:29.767543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.1615` n `231`; crypto_major avg `-0.2639` n `8`; equity avg `-0.1` n `122`; fx avg `-0.0064` n `6`; index avg `-0.0087` n `25`; metal avg `0.0` n `20`; unknown avg `-0.132` n `793`
- 1h: commodity avg `0.0821` n `12`; crypto_alt avg `-0.3471` n `231`; crypto_major avg `-0.312` n `8`; equity avg `0.158` n `122`; fx avg `-0.0284` n `6`; index avg `0.0388` n `25`; metal avg `-0.1242` n `20`; unknown avg `0.0129` n `793`
- 4h: commodity avg `-0.2403` n `12`; crypto_alt avg `0.3036` n `231`; crypto_major avg `0.0927` n `8`; equity avg `-0.3805` n `122`; fx avg `-0.0034` n `6`; index avg `-0.0703` n `25`; metal avg `0.0349` n `20`; unknown avg `0.4237` n `793`
- 24h: commodity avg `-0.1873` n `12`; crypto_alt avg `0.01` n `231`; crypto_major avg `0.6956` n `8`; equity avg `-2.0983` n `122`; fx avg `-0.1483` n `6`; index avg `-0.2565` n `25`; metal avg `0.1936` n `20`; unknown avg `3.6653` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
