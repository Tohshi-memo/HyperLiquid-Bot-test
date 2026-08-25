# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T20:16:37.408062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0989` n `12`; crypto_alt avg `-0.066` n `231`; crypto_major avg `-0.0314` n `8`; equity avg `0.0318` n `122`; fx avg `0.002` n `6`; index avg `0.0003` n `25`; metal avg `-0.001` n `20`; unknown avg `0.0251` n `795`
- 1h: commodity avg `-0.3917` n `12`; crypto_alt avg `-0.7447` n `231`; crypto_major avg `-0.7504` n `8`; equity avg `0.2383` n `122`; fx avg `-0.0001` n `6`; index avg `0.0562` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0127` n `795`
- 4h: commodity avg `-0.294` n `12`; crypto_alt avg `-0.788` n `231`; crypto_major avg `-0.4407` n `8`; equity avg `0.1152` n `122`; fx avg `0.0075` n `6`; index avg `0.0298` n `25`; metal avg `0.134` n `20`; unknown avg `-0.3046` n `795`
- 24h: commodity avg `-0.8285` n `12`; crypto_alt avg `-1.0486` n `231`; crypto_major avg `0.3582` n `8`; equity avg `2.1794` n `122`; fx avg `0.053` n `6`; index avg `0.2631` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.4268` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
