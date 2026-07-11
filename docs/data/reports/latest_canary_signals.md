# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T09:07:25.963879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.1315` n `230`; crypto_major avg `0.0844` n `8`; equity avg `-0.0141` n `92`; fx avg `-0.0075` n `6`; index avg `-0.0021` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0485` n `765`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `0.2627` n `230`; crypto_major avg `0.205` n `8`; equity avg `-0.0037` n `92`; fx avg `-0.0028` n `6`; index avg `-0.0028` n `25`; metal avg `0.0042` n `20`; unknown avg `0.0505` n `765`
- 4h: commodity avg `0.0583` n `12`; crypto_alt avg `0.2866` n `230`; crypto_major avg `0.2863` n `8`; equity avg `0.1322` n `92`; fx avg `0.0079` n `6`; index avg `0.0095` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0312` n `733`
- 24h: commodity avg `-0.1755` n `12`; crypto_alt avg `0.3097` n `229`; crypto_major avg `-0.3487` n `8`; equity avg `0.281` n `92`; fx avg `-0.0734` n `6`; index avg `0.1847` n `25`; metal avg `0.1833` n `20`; unknown avg `2.9182` n `731`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
