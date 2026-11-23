# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T20:22:36.129494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3635` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2339` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0465` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0159` n `13`; crypto_alt avg `0.1186` n `239`; crypto_major avg `0.173` n `8`; equity avg `0.512` n `166`; fx avg `0.0018` n `6`; index avg `0.0587` n `27`; metal avg `0.0334` n `20`; unknown avg `1.7978` n `1264`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.389` n `239`; crypto_major avg `-0.3759` n `8`; equity avg `-0.1458` n `166`; fx avg `0.0107` n `6`; index avg `-0.0191` n `27`; metal avg `-0.0617` n `20`; unknown avg `447.2931` n `1256`
- 4h: commodity avg `0.055` n `13`; crypto_alt avg `-2.1376` n `239`; crypto_major avg `-2.3085` n `8`; equity avg `-0.8279` n `166`; fx avg `-0.0137` n `6`; index avg `-0.0746` n `27`; metal avg `-0.262` n `20`; unknown avg `324.4849` n `1258`
- 24h: commodity avg `-1.5502` n `13`; crypto_alt avg `1.6072` n `239`; crypto_major avg `2.037` n `8`; equity avg `5.9427` n `166`; fx avg `-0.0876` n `6`; index avg `0.571` n `27`; metal avg `0.614` n `20`; unknown avg `6.429` n `1062`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
