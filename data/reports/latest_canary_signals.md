# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T03:52:23.908690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.47` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.8194` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4723` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0178` n `13`; crypto_alt avg `-0.1323` n `239`; crypto_major avg `-0.0911` n `8`; equity avg `-0.1112` n `158`; fx avg `0.0066` n `6`; index avg `0.0077` n `27`; metal avg `0.0318` n `20`; unknown avg `0.0928` n `1264`
- 1h: commodity avg `0.104` n `13`; crypto_alt avg `-0.4842` n `239`; crypto_major avg `-0.2533` n `8`; equity avg `-0.448` n `158`; fx avg `-0.0133` n `6`; index avg `0.0051` n `27`; metal avg `-0.0338` n `20`; unknown avg `0.9381` n `1258`
- 4h: commodity avg `-0.339` n `13`; crypto_alt avg `-2.3081` n `239`; crypto_major avg `-2.0648` n `8`; equity avg `-3.4185` n `158`; fx avg `-0.0512` n `6`; index avg `-0.5925` n `27`; metal avg `-0.2454` n `20`; unknown avg `3.5499` n `1252`
- 24h: commodity avg `-0.13` n `13`; crypto_alt avg `-0.4366` n `239`; crypto_major avg `-0.6795` n `8`; equity avg `-1.2495` n `158`; fx avg `0.1216` n `6`; index avg `-0.3774` n `27`; metal avg `-0.4084` n `20`; unknown avg `-0.4215` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
