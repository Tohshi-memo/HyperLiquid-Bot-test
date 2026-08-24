# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T22:22:28.936300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.0912` n `231`; crypto_major avg `0.016` n `8`; equity avg `-0.0127` n `122`; fx avg `0.0145` n `6`; index avg `-0.004` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.003` n `794`
- 1h: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.1742` n `231`; crypto_major avg `0.0665` n `8`; equity avg `-0.0178` n `122`; fx avg `0.0261` n `6`; index avg `-0.0026` n `25`; metal avg `0.0377` n `20`; unknown avg `-0.118` n `794`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.0651` n `231`; crypto_major avg `0.2457` n `8`; equity avg `-0.4884` n `122`; fx avg `0.0081` n `6`; index avg `-0.0749` n `25`; metal avg `0.1057` n `20`; unknown avg `-0.5426` n `794`
- 24h: commodity avg `-0.1917` n `12`; crypto_alt avg `-1.6343` n `231`; crypto_major avg `-0.7788` n `8`; equity avg `-2.6875` n `122`; fx avg `-0.0641` n `6`; index avg `-0.3184` n `25`; metal avg `0.1338` n `20`; unknown avg `0.8096` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
