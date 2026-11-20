# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T18:22:34.081956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.7036` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.229` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.2044` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0493` n `13`; crypto_alt avg `0.5312` n `239`; crypto_major avg `0.4356` n `8`; equity avg `0.1602` n `166`; fx avg `0.0156` n `6`; index avg `0.0195` n `27`; metal avg `0.0364` n `20`; unknown avg `1.9368` n `1260`
- 1h: commodity avg `-0.0215` n `13`; crypto_alt avg `1.0395` n `239`; crypto_major avg `0.5514` n `8`; equity avg `0.3477` n `166`; fx avg `-0.0051` n `6`; index avg `0.0109` n `27`; metal avg `0.0558` n `20`; unknown avg `159.5543` n `1258`
- 4h: commodity avg `0.0667` n `13`; crypto_alt avg `-2.7246` n `239`; crypto_major avg `-3.6369` n `8`; equity avg `-3.8071` n `166`; fx avg `0.0259` n `6`; index avg `-0.4079` n `27`; metal avg `-0.4325` n `20`; unknown avg `226.7513` n `1249`
- 24h: commodity avg `-0.3082` n `13`; crypto_alt avg `-5.5705` n `239`; crypto_major avg `-6.6662` n `8`; equity avg `-7.8683` n `166`; fx avg `0.0226` n `6`; index avg `-0.7227` n `27`; metal avg `-1.2332` n `20`; unknown avg `42.6718` n `1155`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
