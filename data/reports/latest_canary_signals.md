# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T02:07:26.133853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0933` n `13`; crypto_alt avg `0.6422` n `239`; crypto_major avg `0.9247` n `8`; equity avg `0.6003` n `168`; fx avg `0.0186` n `6`; index avg `0.0541` n `27`; metal avg `0.4711` n `20`; unknown avg `1.4351` n `1249`
- 1h: commodity avg `0.1246` n `13`; crypto_alt avg `0.5219` n `239`; crypto_major avg `0.8275` n `8`; equity avg `1.2002` n `168`; fx avg `0.0322` n `6`; index avg `0.128` n `27`; metal avg `0.6988` n `20`; unknown avg `169.041` n `1257`
- 4h: commodity avg `0.2413` n `13`; crypto_alt avg `0.6184` n `239`; crypto_major avg `0.9641` n `8`; equity avg `1.1981` n `168`; fx avg `0.0094` n `6`; index avg `0.1394` n `27`; metal avg `0.7578` n `20`; unknown avg `211.6038` n `1207`
- 24h: commodity avg `0.3008` n `13`; crypto_alt avg `1.0081` n `239`; crypto_major avg `0.9848` n `8`; equity avg `1.2935` n `168`; fx avg `0.062` n `6`; index avg `0.1299` n `27`; metal avg `0.7319` n `20`; unknown avg `181.5343` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
