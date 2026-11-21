# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T06:37:27.651748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.905` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.8775` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.8125` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0949` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0248` n `13`; crypto_alt avg `0.7468` n `239`; crypto_major avg `1.0721` n `8`; equity avg `0.3216` n `166`; fx avg `-0.087` n `6`; index avg `0.0305` n `27`; metal avg `0.0289` n `20`; unknown avg `12.9048` n `1258`
- 1h: commodity avg `0.0244` n `13`; crypto_alt avg `0.4504` n `239`; crypto_major avg `0.9222` n `8`; equity avg `0.3302` n `166`; fx avg `-0.0905` n `6`; index avg `0.0333` n `27`; metal avg `0.0603` n `20`; unknown avg `328.0359` n `1228`
- 4h: commodity avg `-0.0155` n `13`; crypto_alt avg `-2.8234` n `239`; crypto_major avg `-2.9205` n `8`; equity avg `-0.8256` n `166`; fx avg `-0.1156` n `6`; index avg `-0.043` n `27`; metal avg `-0.108` n `20`; unknown avg `33.6924` n `1214`
- 24h: commodity avg `0.3935` n `13`; crypto_alt avg `-6.764` n `239`; crypto_major avg `-8.3103` n `8`; equity avg `-5.3596` n `166`; fx avg `-0.1605` n `6`; index avg `-0.5495` n `27`; metal avg `-0.3209` n `20`; unknown avg `17.3635` n `1107`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
