# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T04:22:30.271974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.6632` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.5852` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.5158` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-3.3426` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `3.3033` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-3.233` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-3.2321` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.1071` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `0.2774` n `239`; crypto_major avg `0.1156` n `8`; equity avg `-0.1255` n `166`; fx avg `0.0096` n `6`; index avg `-0.0089` n `27`; metal avg `0.0307` n `20`; unknown avg `-0.3189` n `1256`
- 1h: commodity avg `-0.0817` n `13`; crypto_alt avg `-3.0315` n `239`; crypto_major avg `-3.4243` n `8`; equity avg `-1.3172` n `166`; fx avg `-0.0164` n `6`; index avg `-0.121` n `27`; metal avg `-0.1922` n `20`; unknown avg `3.0013` n `1246`
- 4h: commodity avg `-0.0682` n `13`; crypto_alt avg `-4.063` n `239`; crypto_major avg `-4.7314` n `8`; equity avg `-1.4984` n `166`; fx avg `-0.0099` n `6`; index avg `-0.1462` n `27`; metal avg `-0.2156` n `20`; unknown avg `2.0057` n `1244`
- 24h: commodity avg `0.2494` n `13`; crypto_alt avg `-7.3607` n `239`; crypto_major avg `-9.3492` n `8`; equity avg `-6.3374` n `166`; fx avg `-0.0552` n `6`; index avg `-0.6474` n `27`; metal avg `-0.2092` n `20`; unknown avg `12.4535` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
