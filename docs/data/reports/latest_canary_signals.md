# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T08:22:26.285269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `13`; crypto_alt avg `0.1442` n `239`; crypto_major avg `0.1593` n `8`; equity avg `0.3356` n `168`; fx avg `-0.0402` n `6`; index avg `0.0311` n `27`; metal avg `0.0837` n `20`; unknown avg `1.4886` n `1221`
- 1h: commodity avg `-0.0523` n `13`; crypto_alt avg `0.0585` n `239`; crypto_major avg `0.1891` n `8`; equity avg `0.3504` n `168`; fx avg `-0.0621` n `6`; index avg `0.0235` n `27`; metal avg `0.092` n `20`; unknown avg `5.5435` n `1189`
- 4h: commodity avg `-0.0692` n `13`; crypto_alt avg `0.4259` n `239`; crypto_major avg `0.6697` n `8`; equity avg `1.0008` n `168`; fx avg `-0.0913` n `6`; index avg `0.0018` n `27`; metal avg `0.4238` n `20`; unknown avg `6.8698` n `1171`
- 24h: commodity avg `0.3357` n `13`; crypto_alt avg `2.2675` n `239`; crypto_major avg `3.1003` n `8`; equity avg `4.2405` n `168`; fx avg `-0.098` n `6`; index avg `0.3294` n `27`; metal avg `1.3617` n `20`; unknown avg `223.0451` n `975`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
