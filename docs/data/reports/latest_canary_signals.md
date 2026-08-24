# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T15:52:59.911438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0225` n `12`; crypto_alt avg `-0.6993` n `231`; crypto_major avg `-0.7177` n `8`; equity avg `0.058` n `122`; fx avg `-0.004` n `6`; index avg `0.0241` n `25`; metal avg `-0.149` n `20`; unknown avg `0.1276` n `793`
- 1h: commodity avg `-0.0945` n `12`; crypto_alt avg `-0.0284` n `231`; crypto_major avg `-0.2991` n `8`; equity avg `0.4368` n `122`; fx avg `-0.0184` n `6`; index avg `0.0658` n `25`; metal avg `-0.053` n `20`; unknown avg `0.1209` n `793`
- 4h: commodity avg `-0.25` n `12`; crypto_alt avg `0.1309` n `231`; crypto_major avg `0.1301` n `8`; equity avg `-0.644` n `122`; fx avg `-0.0043` n `6`; index avg `-0.1297` n `25`; metal avg `0.0816` n `20`; unknown avg `0.6513` n `793`
- 24h: commodity avg `-0.2691` n `12`; crypto_alt avg `-0.5272` n `231`; crypto_major avg `0.4014` n `8`; equity avg `-2.1904` n `122`; fx avg `-0.1242` n `6`; index avg `-0.2711` n `25`; metal avg `0.1824` n `20`; unknown avg `3.3402` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
