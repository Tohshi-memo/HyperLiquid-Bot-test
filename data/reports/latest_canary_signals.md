# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T17:52:25.680840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.7292` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.5768` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.552` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0345` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0387` n `13`; crypto_alt avg `-0.0862` n `239`; crypto_major avg `-0.2794` n `8`; equity avg `-0.0648` n `168`; fx avg `-0.0082` n `6`; index avg `-0.0188` n `27`; metal avg `-0.045` n `20`; unknown avg `0.9144` n `1264`
- 1h: commodity avg `-0.0201` n `13`; crypto_alt avg `-0.515` n `239`; crypto_major avg `-0.9645` n `8`; equity avg `-0.4479` n `168`; fx avg `-0.0086` n `6`; index avg `-0.044` n `27`; metal avg `-0.0529` n `20`; unknown avg `1.4879` n `1256`
- 4h: commodity avg `-0.1745` n `13`; crypto_alt avg `-2.0201` n `239`; crypto_major avg `-2.7513` n `8`; equity avg `-0.7168` n `168`; fx avg `-0.0726` n `6`; index avg `-0.0221` n `27`; metal avg `-0.1993` n `20`; unknown avg `9.6659` n `1246`
- 24h: commodity avg `-0.5414` n `13`; crypto_alt avg `0.0967` n `239`; crypto_major avg `0.2018` n `8`; equity avg `2.8984` n `168`; fx avg `-0.1515` n `6`; index avg `0.2692` n `27`; metal avg `0.712` n `20`; unknown avg `86.2495` n `1033`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
