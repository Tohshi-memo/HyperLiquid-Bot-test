# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T04:52:24.635788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7989` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3508` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `-0.0601` n `229`; crypto_major avg `-0.0393` n `8`; equity avg `0.0135` n `91`; fx avg `-0.0082` n `6`; index avg `0.0032` n `25`; metal avg `-0.0214` n `20`; unknown avg `0.0376` n `763`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.2035` n `229`; crypto_major avg `-0.1885` n `8`; equity avg `-0.5659` n `91`; fx avg `-0.0257` n `6`; index avg `-0.1543` n `25`; metal avg `-0.0447` n `20`; unknown avg `0.1458` n `763`
- 4h: commodity avg `0.076` n `12`; crypto_alt avg `-1.616` n `229`; crypto_major avg `-1.669` n `8`; equity avg `-0.502` n `91`; fx avg `-0.0806` n `6`; index avg `-0.3182` n `25`; metal avg `0.1299` n `20`; unknown avg `0.4061` n `763`
- 24h: commodity avg `0.9465` n `12`; crypto_alt avg `-2.4822` n `229`; crypto_major avg `-1.7845` n `8`; equity avg `-1.0273` n `91`; fx avg `-0.1812` n `6`; index avg `-0.2067` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.21` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
