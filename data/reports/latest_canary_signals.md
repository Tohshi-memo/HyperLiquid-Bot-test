# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T01:22:24.999966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7423` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5601` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5124` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0473` n `13`; crypto_alt avg `-0.1115` n `238`; crypto_major avg `-0.3488` n `8`; equity avg `-0.0396` n `156`; fx avg `0.0116` n `6`; index avg `-0.0135` n `27`; metal avg `0.047` n `20`; unknown avg `4.2203` n `1260`
- 1h: commodity avg `-0.0187` n `13`; crypto_alt avg `0.7135` n `238`; crypto_major avg `0.4038` n `8`; equity avg `-0.8443` n `156`; fx avg `0.0298` n `6`; index avg `-0.1525` n `27`; metal avg `-0.1752` n `20`; unknown avg `3.2013` n `1254`
- 4h: commodity avg `-0.018` n `13`; crypto_alt avg `-3.6903` n `238`; crypto_major avg `-2.7603` n `8`; equity avg `-1.3926` n `156`; fx avg `0.0272` n `6`; index avg `-0.2002` n `27`; metal avg `-0.2479` n `20`; unknown avg `7.7654` n `1240`
- 24h: commodity avg `-0.2814` n `13`; crypto_alt avg `-7.555` n `238`; crypto_major avg `-3.5027` n `8`; equity avg `-4.1974` n `155`; fx avg `0.1897` n `6`; index avg `-0.4154` n `27`; metal avg `-0.8768` n `20`; unknown avg `33.3648` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
