# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T22:48:22.709177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.0473` n `231`; crypto_major avg `-0.0142` n `8`; equity avg `-0.0081` n `122`; fx avg `-0.0006` n `6`; index avg `-0.0002` n `25`; metal avg `0.0152` n `20`; unknown avg `0.1021` n `794`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.2395` n `231`; crypto_major avg `-0.0462` n `8`; equity avg `-0.0434` n `122`; fx avg `-0.005` n `6`; index avg `0.0011` n `25`; metal avg `0.0674` n `20`; unknown avg `-0.1328` n `794`
- 4h: commodity avg `-0.1193` n `12`; crypto_alt avg `0.1652` n `231`; crypto_major avg `0.5189` n `8`; equity avg `-0.4055` n `122`; fx avg `-0.0071` n `6`; index avg `-0.0518` n `25`; metal avg `0.1654` n `20`; unknown avg `-0.4554` n `794`
- 24h: commodity avg `-0.1513` n `12`; crypto_alt avg `-1.6995` n `231`; crypto_major avg `-0.9361` n `8`; equity avg `-2.7914` n `122`; fx avg `-0.0687` n `6`; index avg `-0.3535` n `25`; metal avg `0.2459` n `20`; unknown avg `1.4079` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
