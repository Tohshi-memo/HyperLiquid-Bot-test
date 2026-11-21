# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T03:22:35.841596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6027` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5854` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3022` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `0.0159` n `239`; crypto_major avg `0.007` n `8`; equity avg `-0.0956` n `166`; fx avg `0.0006` n `6`; index avg `-0.0158` n `27`; metal avg `0.0077` n `20`; unknown avg `0.2027` n `1258`
- 1h: commodity avg `0.0233` n `13`; crypto_alt avg `-1.2299` n `239`; crypto_major avg `-1.331` n `8`; equity avg `-0.2919` n `166`; fx avg `0.0061` n `6`; index avg `-0.0288` n `27`; metal avg `-0.0307` n `20`; unknown avg `31.8185` n `1256`
- 4h: commodity avg `-0.0014` n `13`; crypto_alt avg `-1.5543` n `239`; crypto_major avg `-1.6485` n `8`; equity avg `-0.6555` n `166`; fx avg `0.0009` n `6`; index avg `-0.0631` n `27`; metal avg `-0.0458` n `20`; unknown avg `2.5665` n `1248`
- 24h: commodity avg `0.3737` n `13`; crypto_alt avg `-5.106` n `239`; crypto_major avg `-6.591` n `8`; equity avg `-5.2976` n `166`; fx avg `-0.0477` n `6`; index avg `-0.5937` n `27`; metal avg `-0.0113` n `20`; unknown avg `12.3997` n `1119`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
