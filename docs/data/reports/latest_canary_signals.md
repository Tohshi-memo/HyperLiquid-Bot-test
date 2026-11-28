# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T00:37:29.127261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2021` n `13`; crypto_alt avg `-0.0034` n `239`; crypto_major avg `0.1033` n `8`; equity avg `-0.0557` n `168`; fx avg `0.0013` n `6`; index avg `-0.0092` n `27`; metal avg `0.006` n `20`; unknown avg `-0.1516` n `1265`
- 1h: commodity avg `-0.2182` n `13`; crypto_alt avg `-0.0422` n `239`; crypto_major avg `0.2268` n `8`; equity avg `0.0443` n `168`; fx avg `0.0046` n `6`; index avg `0.0195` n `27`; metal avg `-0.0068` n `20`; unknown avg `0.6568` n `1249`
- 4h: commodity avg `-0.1772` n `13`; crypto_alt avg `0.134` n `239`; crypto_major avg `-0.0179` n `8`; equity avg `-0.0149` n `168`; fx avg `-0.0139` n `6`; index avg `0.0066` n `27`; metal avg `0.0418` n `20`; unknown avg `-0.1294` n `1159`
- 24h: commodity avg `-0.7823` n `13`; crypto_alt avg `0.3557` n `239`; crypto_major avg `0.3137` n `8`; equity avg `3.4573` n `168`; fx avg `-0.1494` n `6`; index avg `0.3529` n `27`; metal avg `1.0021` n `20`; unknown avg `211.5455` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
