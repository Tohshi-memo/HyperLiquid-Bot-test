# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T23:52:28.385951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8588` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.8079` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.6908` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.3582` n `238`; crypto_major avg `-0.6328` n `8`; equity avg `-0.079` n `156`; fx avg `-0.0037` n `6`; index avg `0.0216` n `27`; metal avg `-0.0188` n `20`; unknown avg `0.5897` n `1260`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.8461` n `238`; crypto_major avg `-0.9527` n `8`; equity avg `-0.0155` n `156`; fx avg `-0.0083` n `6`; index avg `0.0341` n `27`; metal avg `-0.0732` n `20`; unknown avg `8.1952` n `1254`
- 4h: commodity avg `-0.0657` n `13`; crypto_alt avg `-5.3318` n `238`; crypto_major avg `-3.9245` n `8`; equity avg `-2.8719` n `156`; fx avg `0.031` n `6`; index avg `-0.2337` n `27`; metal avg `-0.1166` n `20`; unknown avg `11.4379` n `1162`
- 24h: commodity avg `-0.2015` n `13`; crypto_alt avg `-6.3599` n `238`; crypto_major avg `-3.0063` n `8`; equity avg `-3.3663` n `155`; fx avg `0.0901` n `6`; index avg `-0.2327` n `27`; metal avg `-0.6476` n `20`; unknown avg `29.5546` n `996`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
