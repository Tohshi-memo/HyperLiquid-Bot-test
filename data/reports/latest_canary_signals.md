# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T05:46:41.861463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0619` n `12`; crypto_alt avg `0.0769` n `231`; crypto_major avg `0.0021` n `8`; equity avg `0.01` n `122`; fx avg `-0.0058` n `6`; index avg `0.0061` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0393` n `797`
- 1h: commodity avg `0.102` n `12`; crypto_alt avg `0.251` n `231`; crypto_major avg `0.3228` n `8`; equity avg `-0.1266` n `122`; fx avg `-0.0073` n `6`; index avg `-0.0118` n `25`; metal avg `0.0069` n `20`; unknown avg `7.0858` n `797`
- 4h: commodity avg `0.0907` n `12`; crypto_alt avg `0.4018` n `231`; crypto_major avg `0.4256` n `8`; equity avg `0.5986` n `122`; fx avg `0.0055` n `6`; index avg `0.1441` n `25`; metal avg `-0.0365` n `20`; unknown avg `8.1881` n `796`
- 24h: commodity avg `-0.5347` n `12`; crypto_alt avg `-2.8972` n `231`; crypto_major avg `-2.7258` n `8`; equity avg `0.8449` n `122`; fx avg `-0.0082` n `6`; index avg `0.129` n `25`; metal avg `0.2532` n `20`; unknown avg `0.5742` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
