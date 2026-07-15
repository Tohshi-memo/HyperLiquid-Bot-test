# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T06:07:26.388995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `0.312` n `230`; crypto_major avg `0.3305` n `8`; equity avg `0.1804` n `93`; fx avg `0.0142` n `6`; index avg `0.0376` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.0286` n `749`
- 1h: commodity avg `-0.0166` n `12`; crypto_alt avg `0.3526` n `230`; crypto_major avg `0.5406` n `8`; equity avg `0.1674` n `93`; fx avg `-0.0285` n `6`; index avg `0.0331` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0267` n `749`
- 4h: commodity avg `-0.0857` n `12`; crypto_alt avg `0.2927` n `230`; crypto_major avg `0.942` n `8`; equity avg `0.5411` n `93`; fx avg `-0.0034` n `6`; index avg `0.0665` n `25`; metal avg `-0.0504` n `20`; unknown avg `0.2211` n `749`
- 24h: commodity avg `0.1118` n `12`; crypto_alt avg `1.7965` n `230`; crypto_major avg `3.5219` n `8`; equity avg `1.8616` n `92`; fx avg `0.0874` n `6`; index avg `0.5123` n `25`; metal avg `0.2191` n `20`; unknown avg `0.3423` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
