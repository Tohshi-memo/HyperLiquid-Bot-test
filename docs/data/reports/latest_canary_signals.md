# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T21:52:30.689789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.7996` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.7465` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5977` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `-1.3016` n `238`; crypto_major avg `-1.001` n `8`; equity avg `-0.1994` n `156`; fx avg `-0.0036` n `6`; index avg `-0.0026` n `27`; metal avg `-0.0024` n `20`; unknown avg `1.984` n `1258`
- 1h: commodity avg `-0.0408` n `13`; crypto_alt avg `-0.1051` n `238`; crypto_major avg `0.165` n `8`; equity avg `-0.5947` n `156`; fx avg `-0.0193` n `6`; index avg `-0.0468` n `27`; metal avg `-0.0056` n `20`; unknown avg `155.6437` n `1246`
- 4h: commodity avg `0.0042` n `13`; crypto_alt avg `-4.5942` n `238`; crypto_major avg `-2.7423` n `8`; equity avg `-2.3699` n `156`; fx avg `0.0` n `6`; index avg `-0.1446` n `27`; metal avg `0.0573` n `20`; unknown avg `24.3439` n `1162`
- 24h: commodity avg `-0.257` n `13`; crypto_alt avg `-5.9184` n `238`; crypto_major avg `-2.0687` n `8`; equity avg `-3.2656` n `155`; fx avg `0.0432` n `6`; index avg `-0.2555` n `27`; metal avg `-0.5953` n `20`; unknown avg `32.8496` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
