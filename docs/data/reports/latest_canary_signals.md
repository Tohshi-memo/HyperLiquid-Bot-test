# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T05:07:26.313853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.665` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0342` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0444` n `12`; crypto_alt avg `0.3328` n `229`; crypto_major avg `0.2672` n `8`; equity avg `0.2709` n `91`; fx avg `0.0026` n `6`; index avg `0.0632` n `25`; metal avg `0.108` n `20`; unknown avg `-0.053` n `763`
- 1h: commodity avg `0.0493` n `12`; crypto_alt avg `0.1983` n `229`; crypto_major avg `0.1352` n `8`; equity avg `-0.1586` n `91`; fx avg `-0.0195` n `6`; index avg `-0.064` n `25`; metal avg `0.1051` n `20`; unknown avg `0.0229` n `763`
- 4h: commodity avg `0.1072` n `12`; crypto_alt avg `-1.1577` n `229`; crypto_major avg `-1.244` n `8`; equity avg `-0.0609` n `91`; fx avg `-0.0726` n `6`; index avg `-0.2098` n `25`; metal avg `0.421` n `20`; unknown avg `0.3107` n `763`
- 24h: commodity avg `0.99` n `12`; crypto_alt avg `-2.095` n `229`; crypto_major avg `-1.4884` n `8`; equity avg `-0.6082` n `91`; fx avg `-0.2025` n `6`; index avg `-0.1222` n `25`; metal avg `0.1405` n `20`; unknown avg `-0.1823` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
