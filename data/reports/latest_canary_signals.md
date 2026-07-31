# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T18:38:31.153470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1123` n `12`; crypto_alt avg `-0.241` n `230`; crypto_major avg `-0.2906` n `8`; equity avg `0.0` n `102`; fx avg `0.0019` n `6`; index avg `-0.0035` n `25`; metal avg `0.0183` n `20`; unknown avg `-0.1681` n `780`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `-0.2666` n `230`; crypto_major avg `-0.2799` n `8`; equity avg `-0.2341` n `102`; fx avg `0.0739` n `6`; index avg `-0.0334` n `25`; metal avg `0.0498` n `20`; unknown avg `7.3039` n `780`
- 4h: commodity avg `-0.1024` n `12`; crypto_alt avg `0.2931` n `230`; crypto_major avg `-0.2082` n `8`; equity avg `0.4147` n `102`; fx avg `0.1045` n `6`; index avg `0.1474` n `25`; metal avg `0.2194` n `20`; unknown avg `9.0362` n `780`
- 24h: commodity avg `0.1728` n `12`; crypto_alt avg `-0.2141` n `230`; crypto_major avg `-1.8358` n `8`; equity avg `0.8306` n `102`; fx avg `0.2359` n `6`; index avg `0.3361` n `25`; metal avg `-0.2695` n `20`; unknown avg `0.3983` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
