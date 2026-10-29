# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T02:37:29.274305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3483` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.138` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1133` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2821` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0418` n `13`; crypto_alt avg `-0.5631` n `238`; crypto_major avg `-0.3747` n `8`; equity avg `-0.2298` n `155`; fx avg `-0.0046` n `6`; index avg `-0.0372` n `27`; metal avg `-0.0929` n `20`; unknown avg `0.2123` n `1234`
- 1h: commodity avg `-0.0574` n `13`; crypto_alt avg `-1.9301` n `238`; crypto_major avg `-1.3985` n `8`; equity avg `-0.8538` n `155`; fx avg `0.0213` n `6`; index avg `-0.1164` n `27`; metal avg `-0.1687` n `20`; unknown avg `2.215` n `1228`
- 4h: commodity avg `0.052` n `13`; crypto_alt avg `-2.9816` n `238`; crypto_major avg `-2.2963` n `8`; equity avg `-1.1672` n `155`; fx avg `-0.1034` n `6`; index avg `-0.1583` n `27`; metal avg `-0.183` n `20`; unknown avg `4.672` n `1156`
- 24h: commodity avg `-0.0218` n `13`; crypto_alt avg `-2.7118` n `238`; crypto_major avg `-1.9704` n `8`; equity avg `-1.2439` n `154`; fx avg `0.0002` n `6`; index avg `-0.1786` n `27`; metal avg `-0.2414` n `20`; unknown avg `25.7261` n `992`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
