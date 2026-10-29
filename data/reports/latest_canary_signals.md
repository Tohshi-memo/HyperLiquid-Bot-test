# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T21:37:28.498361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.4054` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.4038` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2405` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0081` n `13`; crypto_alt avg `0.4792` n `238`; crypto_major avg `0.5528` n `8`; equity avg `0.1477` n `156`; fx avg `-0.0077` n `6`; index avg `0.0189` n `27`; metal avg `0.0108` n `20`; unknown avg `0.2129` n `1260`
- 1h: commodity avg `-0.0221` n `13`; crypto_alt avg `-1.0174` n `238`; crypto_major avg `0.2003` n `8`; equity avg `-0.9977` n `156`; fx avg `-0.0139` n `6`; index avg `-0.0778` n `27`; metal avg `-0.0704` n `20`; unknown avg `174.3452` n `1244`
- 4h: commodity avg `-0.0112` n `13`; crypto_alt avg `-4.1013` n `238`; crypto_major avg `-2.415` n `8`; equity avg `-2.4568` n `156`; fx avg `-0.008` n `6`; index avg `-0.1745` n `27`; metal avg `-0.0096` n `20`; unknown avg `24.4941` n `1162`
- 24h: commodity avg `-0.2569` n `13`; crypto_alt avg `-4.3499` n `238`; crypto_major avg `-0.7554` n `8`; equity avg `-2.8713` n `155`; fx avg `0.0455` n `6`; index avg `-0.2217` n `27`; metal avg `-0.5832` n `20`; unknown avg `33.9107` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
