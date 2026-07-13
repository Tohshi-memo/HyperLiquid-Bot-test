# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T21:07:28.041899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0484` n `12`; crypto_alt avg `0.0882` n `230`; crypto_major avg `0.0838` n `8`; equity avg `0.0528` n `92`; fx avg `0.0028` n `6`; index avg `0.0131` n `25`; metal avg `0.0162` n `20`; unknown avg `0.0881` n `766`
- 1h: commodity avg `0.0211` n `12`; crypto_alt avg `-0.3147` n `230`; crypto_major avg `-0.301` n `8`; equity avg `-0.0388` n `92`; fx avg `-0.0105` n `6`; index avg `-0.0595` n `25`; metal avg `-0.0216` n `20`; unknown avg `-0.1486` n `766`
- 4h: commodity avg `0.4301` n `12`; crypto_alt avg `-0.7025` n `230`; crypto_major avg `-0.2996` n `8`; equity avg `-0.3814` n `92`; fx avg `-0.0334` n `6`; index avg `-0.1388` n `25`; metal avg `0.0113` n `20`; unknown avg `-0.4057` n `766`
- 24h: commodity avg `0.5683` n `12`; crypto_alt avg `-2.5574` n `230`; crypto_major avg `-3.1459` n `8`; equity avg `-3.2827` n `92`; fx avg `-0.0398` n `6`; index avg `-0.6829` n `25`; metal avg `-0.5318` n `20`; unknown avg `-0.3498` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
