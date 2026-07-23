# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T16:12:09.814093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1391` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.1028` n `230`; crypto_major avg `-0.2508` n `8`; equity avg `0.2878` n `100`; fx avg `0.0072` n `6`; index avg `0.0885` n `25`; metal avg `0.0257` n `20`; unknown avg `-0.1586` n `772`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0621` n `230`; crypto_major avg `-0.1006` n `8`; equity avg `0.3544` n `100`; fx avg `0.0025` n `6`; index avg `0.06` n `25`; metal avg `-0.0246` n `20`; unknown avg `-0.1284` n `772`
- 4h: commodity avg `0.2105` n `12`; crypto_alt avg `-0.7384` n `230`; crypto_major avg `-1.3693` n `8`; equity avg `-0.884` n `99`; fx avg `-0.0198` n `6`; index avg `-0.2302` n `25`; metal avg `-0.3143` n `20`; unknown avg `0.0233` n `772`
- 24h: commodity avg `1.1038` n `12`; crypto_alt avg `-1.3697` n `230`; crypto_major avg `-1.8763` n `8`; equity avg `-1.8747` n `99`; fx avg `-0.0788` n `6`; index avg `-0.3829` n `25`; metal avg `-0.9278` n `20`; unknown avg `-0.3153` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
