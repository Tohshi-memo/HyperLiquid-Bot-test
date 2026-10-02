# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T15:06:16.024154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7869` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5548` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `-0.7107` n `235`; crypto_major avg `-0.667` n `8`; equity avg `-0.3889` n `143`; fx avg `-0.0014` n `6`; index avg `-0.0794` n `26`; metal avg `-0.1936` n `20`; unknown avg `4.3405` n `982`
- 1h: commodity avg `0.1156` n `13`; crypto_alt avg `-0.9229` n `235`; crypto_major avg `-1.052` n `8`; equity avg `-0.4566` n `143`; fx avg `0.0024` n `6`; index avg `-0.0927` n `26`; metal avg `-0.3612` n `20`; unknown avg `0.9717` n `958`
- 4h: commodity avg `0.1339` n `13`; crypto_alt avg `-0.4651` n `235`; crypto_major avg `-1.4401` n `8`; equity avg `0.3468` n `142`; fx avg `0.0616` n `6`; index avg `0.1147` n `26`; metal avg `-0.3287` n `20`; unknown avg `0.7405` n `934`
- 24h: commodity avg `-0.6577` n `13`; crypto_alt avg `2.5134` n `235`; crypto_major avg `1.2224` n `8`; equity avg `2.2673` n `142`; fx avg `-0.1709` n `6`; index avg `0.5734` n `26`; metal avg `-0.0551` n `20`; unknown avg `103.6922` n `814`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
