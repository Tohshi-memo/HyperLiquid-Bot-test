# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T16:37:35.778970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0544` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9621` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3927` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1762` n `12`; crypto_alt avg `-0.2667` n `228`; crypto_major avg `-0.1394` n `8`; equity avg `-0.2964` n `77`; fx avg `0.0039` n `6`; index avg `-0.2354` n `23`; metal avg `-0.0319` n `18`; unknown avg `-0.0228` n `687`
- 1h: commodity avg `-0.4013` n `12`; crypto_alt avg `-0.2188` n `228`; crypto_major avg `-0.4613` n `8`; equity avg `-0.1273` n `77`; fx avg `0.0276` n `6`; index avg `-0.2172` n `23`; metal avg `0.252` n `18`; unknown avg `-0.1158` n `687`
- 4h: commodity avg `-0.0762` n `12`; crypto_alt avg `-2.0176` n `228`; crypto_major avg `-2.1306` n `8`; equity avg `-1.1229` n `77`; fx avg `0.0686` n `6`; index avg `-0.7379` n `23`; metal avg `-0.1685` n `18`; unknown avg `1.5915` n `687`
- 24h: commodity avg `-1.0245` n `12`; crypto_alt avg `-2.5488` n `228`; crypto_major avg `-1.7761` n `8`; equity avg `-1.1062` n `77`; fx avg `-0.0184` n `6`; index avg `-0.8686` n `23`; metal avg `0.3419` n `18`; unknown avg `0.3341` n `623`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0428`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
