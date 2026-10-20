# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T21:22:33.218524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `-0.0291` n `237`; crypto_major avg `0.0865` n `8`; equity avg `-0.0485` n `151`; fx avg `0.0144` n `6`; index avg `-0.0047` n `26`; metal avg `-0.001` n `20`; unknown avg `0.1734` n `1193`
- 1h: commodity avg `0.0764` n `13`; crypto_alt avg `0.7314` n `237`; crypto_major avg `0.5359` n `8`; equity avg `1.0993` n `151`; fx avg `-0.0005` n `6`; index avg `0.1202` n `26`; metal avg `0.0431` n `20`; unknown avg `2.5009` n `1169`
- 4h: commodity avg `0.123` n `13`; crypto_alt avg `0.4771` n `237`; crypto_major avg `0.4868` n `8`; equity avg `0.8636` n `151`; fx avg `0.0047` n `6`; index avg `0.1004` n `26`; metal avg `0.0163` n `20`; unknown avg `15.645` n `1121`
- 24h: commodity avg `-0.0278` n `13`; crypto_alt avg `2.9426` n `237`; crypto_major avg `1.8613` n `8`; equity avg `1.0975` n `151`; fx avg `0.0173` n `6`; index avg `0.1342` n `26`; metal avg `0.0621` n `20`; unknown avg `0.5269` n `1038`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
