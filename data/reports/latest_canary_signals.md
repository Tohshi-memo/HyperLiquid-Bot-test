# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T21:37:31.674916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0678` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8509` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.5937` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5858` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `-0.0837` n `239`; crypto_major avg `-0.1764` n `8`; equity avg `-0.4156` n `165`; fx avg `-0.0131` n `6`; index avg `-0.0338` n `27`; metal avg `-0.2029` n `20`; unknown avg `28.6682` n `1262`
- 1h: commodity avg `0.0268` n `13`; crypto_alt avg `-0.5894` n `239`; crypto_major avg `-0.8081` n `8`; equity avg `-2.028` n `165`; fx avg `-0.0194` n `6`; index avg `-0.1033` n `27`; metal avg `-0.3907` n `20`; unknown avg `3.6082` n `1242`
- 4h: commodity avg `-0.0666` n `13`; crypto_alt avg `-1.2869` n `239`; crypto_major avg `-2.1344` n `8`; equity avg `-3.7281` n `165`; fx avg `-0.0355` n `6`; index avg `-0.2835` n `27`; metal avg `-0.5486` n `20`; unknown avg `14.5595` n `1234`
- 24h: commodity avg `0.0171` n `13`; crypto_alt avg `-1.211` n `239`; crypto_major avg `-0.9383` n `8`; equity avg `-3.877` n `165`; fx avg `-0.0197` n `6`; index avg `-0.2442` n `27`; metal avg `-0.9117` n `20`; unknown avg `11.7542` n `1170`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
