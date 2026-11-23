# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T19:37:29.647847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.664` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.5258` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.3441` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7595` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `-0.7077` n `239`; crypto_major avg `-0.761` n `8`; equity avg `-0.4745` n `166`; fx avg `0.0023` n `6`; index avg `-0.0579` n `27`; metal avg `-0.0899` n `20`; unknown avg `160.8351` n `1266`
- 1h: commodity avg `-0.2557` n `13`; crypto_alt avg `-1.1241` n `239`; crypto_major avg `-0.976` n `8`; equity avg `-0.4173` n `166`; fx avg `-0.0037` n `6`; index avg `-0.042` n `27`; metal avg `-0.0616` n `20`; unknown avg `1.4059` n `1266`
- 4h: commodity avg `-0.0307` n `13`; crypto_alt avg `-2.763` n `239`; crypto_major avg `-3.6947` n `8`; equity avg `-1.9352` n `166`; fx avg `-0.0737` n `6`; index avg `-0.1689` n `27`; metal avg `-0.3506` n `20`; unknown avg `8.016` n `1258`
- 24h: commodity avg `-1.5356` n `13`; crypto_alt avg `1.3577` n `239`; crypto_major avg `1.5069` n `8`; equity avg `5.589` n `166`; fx avg `-0.08` n `6`; index avg `0.5237` n `27`; metal avg `0.5884` n `20`; unknown avg `240.287` n `1064`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
