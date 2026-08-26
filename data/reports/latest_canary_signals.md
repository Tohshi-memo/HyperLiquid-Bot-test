# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T10:22:29.923942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.3486` n `231`; crypto_major avg `0.3615` n `8`; equity avg `0.0057` n `122`; fx avg `-0.0069` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0129` n `20`; unknown avg `0.1745` n `797`
- 1h: commodity avg `0.0725` n `12`; crypto_alt avg `0.1264` n `231`; crypto_major avg `0.2688` n `8`; equity avg `0.0434` n `122`; fx avg `-0.0017` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.1721` n `797`
- 4h: commodity avg `-0.097` n `12`; crypto_alt avg `-0.5175` n `231`; crypto_major avg `-0.2764` n `8`; equity avg `0.0262` n `122`; fx avg `-0.0197` n `6`; index avg `-0.0331` n `25`; metal avg `-0.0941` n `20`; unknown avg `0.1346` n `797`
- 24h: commodity avg `-0.2749` n `12`; crypto_alt avg `-1.8265` n `231`; crypto_major avg `-1.5178` n `8`; equity avg `0.0486` n `122`; fx avg `-0.0435` n `6`; index avg `-0.0739` n `25`; metal avg `0.1428` n `20`; unknown avg `0.806` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
