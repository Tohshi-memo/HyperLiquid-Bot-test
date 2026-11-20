# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T19:22:27.888981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9826` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1976` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.0241` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0087` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6658` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.6429` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0829` n `13`; crypto_alt avg `-0.5235` n `239`; crypto_major avg `-0.7277` n `8`; equity avg `-0.6981` n `166`; fx avg `0.0018` n `6`; index avg `-0.0919` n `27`; metal avg `-0.1241` n `20`; unknown avg `-0.2965` n `1258`
- 1h: commodity avg `0.2816` n `13`; crypto_alt avg `-0.9856` n `239`; crypto_major avg `-1.7425` n `8`; equity avg `-0.6186` n `166`; fx avg `-0.0231` n `6`; index avg `-0.0996` n `27`; metal avg `-0.0767` n `20`; unknown avg `319.9056` n `1256`
- 4h: commodity avg `0.5777` n `13`; crypto_alt avg `-1.1502` n `239`; crypto_major avg `-2.4049` n `8`; equity avg `-2.9562` n `166`; fx avg `0.0071` n `6`; index avg `-0.3962` n `27`; metal avg `-0.2073` n `20`; unknown avg `1.6074` n `1245`
- 24h: commodity avg `0.1185` n `13`; crypto_alt avg `-6.4714` n `239`; crypto_major avg `-7.8468` n `8`; equity avg `-8.4277` n `166`; fx avg `0.0064` n `6`; index avg `-0.8231` n `27`; metal avg `-1.3171` n `20`; unknown avg `35.9835` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
