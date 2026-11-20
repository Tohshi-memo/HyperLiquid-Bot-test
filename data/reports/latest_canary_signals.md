# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T16:32:19.017496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.465` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.2519` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.1669` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0279` n `13`; crypto_alt avg `-0.0409` n `239`; crypto_major avg `-0.0714` n `8`; equity avg `-0.7367` n `166`; fx avg `-0.0044` n `6`; index avg `-0.0746` n `27`; metal avg `-0.0539` n `20`; unknown avg `159.0501` n `1259`
- 1h: commodity avg `0.1891` n `13`; crypto_alt avg `-0.0479` n `239`; crypto_major avg `-0.3347` n `8`; equity avg `-0.8473` n `166`; fx avg `0.0062` n `6`; index avg `-0.1245` n `27`; metal avg `-0.1662` n `20`; unknown avg `0.2199` n `1247`
- 4h: commodity avg `-0.0236` n `13`; crypto_alt avg `-3.1543` n `239`; crypto_major avg `-3.4886` n `8`; equity avg `-2.6681` n `166`; fx avg `-0.0137` n `6`; index avg `-0.2367` n `27`; metal avg `-0.3217` n `20`; unknown avg `0.6063` n `1245`
- 24h: commodity avg `-0.3837` n `13`; crypto_alt avg `-6.0681` n `239`; crypto_major avg `-6.4044` n `8`; equity avg `-9.847` n `166`; fx avg `-0.0357` n `6`; index avg `-0.8895` n `27`; metal avg `-1.2724` n `20`; unknown avg `43.3032` n `1151`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
