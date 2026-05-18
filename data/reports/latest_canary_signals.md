# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T14:52:26.835422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0767` n `12`; crypto_alt avg `-0.1062` n `228`; crypto_major avg `-0.1308` n `8`; equity avg `0.1343` n `66`; fx avg `-0.0236` n `5`; index avg `0.0794` n `23`; metal avg `0.0903` n `18`; unknown avg `-0.0622` n `384`
- 1h: commodity avg `1.0461` n `12`; crypto_alt avg `-0.82` n `228`; crypto_major avg `-0.8237` n `8`; equity avg `-1.1474` n `66`; fx avg `0.0001` n `5`; index avg `-0.4591` n `23`; metal avg `-0.7872` n `18`; unknown avg `0.1841` n `384`
- 4h: commodity avg `-0.2297` n `12`; crypto_alt avg `0.0279` n `228`; crypto_major avg `-0.318` n `8`; equity avg `-1.0558` n `66`; fx avg `-0.0294` n `5`; index avg `-0.2136` n `23`; metal avg `0.3926` n `18`; unknown avg `0.0115` n `383`
- 24h: commodity avg `0.6624` n `12`; crypto_alt avg `-2.7189` n `228`; crypto_major avg `-1.8506` n `8`; equity avg `-0.514` n `66`; fx avg `0.0509` n `5`; index avg `-0.1476` n `23`; metal avg `0.4258` n `18`; unknown avg `-0.409` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
