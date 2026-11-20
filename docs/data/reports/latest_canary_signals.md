# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T19:07:30.245542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.1023` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.3506` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.2537` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.044` n `13`; crypto_alt avg `-0.1809` n `239`; crypto_major avg `-0.4136` n `8`; equity avg `-0.0107` n `166`; fx avg `-0.0157` n `6`; index avg `-0.0209` n `27`; metal avg `0.1031` n `20`; unknown avg `3.1666` n `1252`
- 1h: commodity avg `0.2478` n `13`; crypto_alt avg `0.062` n `239`; crypto_major avg `-0.5922` n `8`; equity avg `0.2407` n `166`; fx avg `-0.0093` n `6`; index avg `0.0117` n `27`; metal avg `0.0841` n `20`; unknown avg `261.4261` n `1256`
- 4h: commodity avg `0.3809` n `13`; crypto_alt avg `-2.7155` n `239`; crypto_major avg `-3.7214` n `8`; equity avg `-3.8301` n `166`; fx avg `0.0161` n `6`; index avg `-0.4677` n `27`; metal avg `-0.3708` n `20`; unknown avg `160.5409` n `1245`
- 24h: commodity avg `-0.0353` n `13`; crypto_alt avg `-5.8133` n `239`; crypto_major avg `-7.0577` n `8`; equity avg `-7.4183` n `166`; fx avg `0.0022` n `6`; index avg `-0.6908` n `27`; metal avg `-1.1613` n `20`; unknown avg `37.9315` n `1147`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
