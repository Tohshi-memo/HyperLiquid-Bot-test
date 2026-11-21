# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T03:34:18.489734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.6517` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.596` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.5109` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.9439` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.9137` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.8167` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.3595` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-2.0923` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0668` n `13`; crypto_alt avg `-2.0881` n `239`; crypto_major avg `-2.1131` n `8`; equity avg `-0.7555` n `166`; fx avg `-0.0218` n `6`; index avg `-0.0685` n `27`; metal avg `-0.163` n `20`; unknown avg `1.6969` n `1260`
- 1h: commodity avg `-0.054` n `13`; crypto_alt avg `-2.8852` n `239`; crypto_major avg `-2.9979` n `8`; equity avg `-0.9056` n `166`; fx avg `-0.0221` n `6`; index avg `-0.0842` n `27`; metal avg `-0.1812` n `20`; unknown avg `109.3873` n `1256`
- 4h: commodity avg `-0.0706` n `13`; crypto_alt avg `-3.6438` n `239`; crypto_major avg `-3.7223` n `8`; equity avg `-1.3628` n `166`; fx avg `-0.0148` n `6`; index avg `-0.1263` n `27`; metal avg `-0.2114` n `20`; unknown avg `1.1403` n `1246`
- 24h: commodity avg `0.2985` n `13`; crypto_alt avg `-6.7686` n `239`; crypto_major avg `-8.3813` n `8`; equity avg `-5.8317` n `166`; fx avg `-0.064` n `6`; index avg `-0.6396` n `27`; metal avg `-0.1861` n `20`; unknown avg `12.4753` n `1115`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
