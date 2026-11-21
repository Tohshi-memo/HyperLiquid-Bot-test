# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T03:37:26.887817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.3623` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.2802` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.2156` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.6529` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.5963` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.5197` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.989` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.7195` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0585` n `13`; crypto_alt avg `-1.6975` n `239`; crypto_major avg `-1.8116` n `8`; equity avg `-0.8289` n `166`; fx avg `-0.0179` n `6`; index avg `-0.0866` n `27`; metal avg `-0.1606` n `20`; unknown avg `5.9192` n `1262`
- 1h: commodity avg `-0.0457` n `13`; crypto_alt avg `-2.4984` n `239`; crypto_major avg `-2.6986` n `8`; equity avg `-0.9791` n `166`; fx avg `-0.0181` n `6`; index avg `-0.1023` n `27`; metal avg `-0.1789` n `20`; unknown avg `110.5315` n `1256`
- 4h: commodity avg `-0.0623` n `13`; crypto_alt avg `-3.2613` n `239`; crypto_major avg `-3.4246` n `8`; equity avg `-1.4356` n `166`; fx avg `-0.0109` n `6`; index avg `-0.1444` n `27`; metal avg `-0.209` n `20`; unknown avg `2.0696` n `1248`
- 24h: commodity avg `0.3071` n `13`; crypto_alt avg `-6.4033` n `239`; crypto_major avg `-8.0996` n `8`; equity avg `-5.8971` n `166`; fx avg `-0.06` n `6`; index avg `-0.657` n `27`; metal avg `-0.1837` n `20`; unknown avg `12.5653` n `1115`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
