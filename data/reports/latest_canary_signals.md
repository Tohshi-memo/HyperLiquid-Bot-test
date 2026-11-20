# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T16:22:35.938947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2409` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.106` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.0166` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0402` n `13`; crypto_alt avg `-0.0023` n `239`; crypto_major avg `-0.2626` n `8`; equity avg `-0.0622` n `166`; fx avg `0.0049` n `6`; index avg `-0.0052` n `27`; metal avg `-0.0259` n `20`; unknown avg `-0.0813` n `1259`
- 1h: commodity avg `0.1331` n `13`; crypto_alt avg `-0.5006` n `239`; crypto_major avg `-0.6767` n `8`; equity avg `-1.2311` n `166`; fx avg `0.0113` n `6`; index avg `-0.1374` n `27`; metal avg `0.0047` n `20`; unknown avg `20.7378` n `1249`
- 4h: commodity avg `-0.0432` n `13`; crypto_alt avg `-3.1121` n `239`; crypto_major avg `-3.2841` n `8`; equity avg `-1.9694` n `166`; fx avg `0.0218` n `6`; index avg `-0.1781` n `27`; metal avg `-0.2675` n `20`; unknown avg `160.3409` n `1249`
- 24h: commodity avg `-0.4822` n `13`; crypto_alt avg `-5.941` n `239`; crypto_major avg `-6.129` n `8`; equity avg `-8.7082` n `166`; fx avg `-0.0259` n `6`; index avg `-0.7613` n `27`; metal avg `-1.1486` n `20`; unknown avg `44.5843` n `1154`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
