# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T15:52:32.974690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.0212` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5722` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1165` n `13`; crypto_alt avg `-0.323` n `239`; crypto_major avg `-0.28` n `8`; equity avg `-0.151` n `168`; fx avg `-0.0151` n `6`; index avg `-0.0046` n `27`; metal avg `-0.0332` n `20`; unknown avg `27.1439` n `1264`
- 1h: commodity avg `-0.1024` n `13`; crypto_alt avg `0.2732` n `239`; crypto_major avg `0.7803` n `8`; equity avg `1.1499` n `168`; fx avg `-0.04` n `6`; index avg `0.1315` n `27`; metal avg `-0.1145` n `20`; unknown avg `2.274` n `1258`
- 4h: commodity avg `-0.3551` n `13`; crypto_alt avg `-1.6961` n `239`; crypto_major avg `-2.0272` n `8`; equity avg `-0.6681` n `168`; fx avg `-0.0417` n `6`; index avg `-0.006` n `27`; metal avg `-0.455` n `20`; unknown avg `1.1402` n `1249`
- 24h: commodity avg `-0.437` n `13`; crypto_alt avg `0.477` n `239`; crypto_major avg `1.0746` n `8`; equity avg `2.5234` n `168`; fx avg `-0.1369` n `6`; index avg `0.2381` n `27`; metal avg `0.6693` n `20`; unknown avg `92.4505` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
