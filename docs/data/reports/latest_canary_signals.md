# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T19:52:27.882935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7056` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5289` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3593` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0302` n `13`; crypto_alt avg `0.2584` n `239`; crypto_major avg `0.3197` n `8`; equity avg `-0.105` n `166`; fx avg `0.0021` n `6`; index avg `-0.0309` n `27`; metal avg `-0.0189` n `20`; unknown avg `157.8604` n `1266`
- 1h: commodity avg `-0.2488` n `13`; crypto_alt avg `-0.7547` n `239`; crypto_major avg `-0.4793` n `8`; equity avg `-0.1921` n `166`; fx avg `0.001` n `6`; index avg `-0.0392` n `27`; metal avg `-0.0859` n `20`; unknown avg `0.709` n `1264`
- 4h: commodity avg `0.0759` n `13`; crypto_alt avg `-1.9535` n `239`; crypto_major avg `-2.6297` n `8`; equity avg `-1.132` n `166`; fx avg `-0.0528` n `6`; index avg `-0.1008` n `27`; metal avg `-0.2704` n `20`; unknown avg `164.4939` n `1260`
- 24h: commodity avg `-1.5665` n `13`; crypto_alt avg `1.5897` n `239`; crypto_major avg `1.7974` n `8`; equity avg `5.4358` n `166`; fx avg `-0.0946` n `6`; index avg `0.487` n `27`; metal avg `0.5641` n `20`; unknown avg `51.1449` n `1060`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
