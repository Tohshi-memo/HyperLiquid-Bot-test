# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T14:52:35.362318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-3.0667` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.8798` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8091` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `2.7695` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.7657` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.5689` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0357` n `13`; crypto_alt avg `-1.2005` n `239`; crypto_major avg `-1.5379` n `8`; equity avg `-0.4106` n `168`; fx avg `0.0053` n `6`; index avg `-0.0371` n `27`; metal avg `0.036` n `20`; unknown avg `1.2823` n `1264`
- 1h: commodity avg `0.121` n `13`; crypto_alt avg `-2.2261` n `239`; crypto_major avg `-2.9457` n `8`; equity avg `-2.029` n `168`; fx avg `-0.006` n `6`; index avg `-0.1762` n `27`; metal avg `-0.0659` n `20`; unknown avg `6.3752` n `1258`
- 4h: commodity avg `-0.2549` n `13`; crypto_alt avg `-2.1199` n `239`; crypto_major avg `-3.0206` n `8`; equity avg `-2.5798` n `168`; fx avg `0.0001` n `6`; index avg `-0.2115` n `27`; metal avg `-0.4517` n `20`; unknown avg `3.0593` n `1251`
- 24h: commodity avg `-0.2459` n `13`; crypto_alt avg `-0.0262` n `239`; crypto_major avg `-0.0466` n `8`; equity avg `1.3438` n `168`; fx avg `-0.0897` n `6`; index avg `0.1045` n `27`; metal avg `0.7535` n `20`; unknown avg `400.6848` n `1031`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
