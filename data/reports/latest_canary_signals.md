# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T06:37:28.488818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.115` n `229`; crypto_major avg `-0.0831` n `8`; equity avg `-0.0793` n `88`; fx avg `-0.0585` n `6`; index avg `-0.0046` n `25`; metal avg `0.0573` n `20`; unknown avg `-0.1579` n `765`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `0.0587` n `229`; crypto_major avg `-0.1371` n `8`; equity avg `0.0417` n `88`; fx avg `-0.1542` n `6`; index avg `0.0393` n `25`; metal avg `-0.0474` n `20`; unknown avg `-0.1515` n `745`
- 4h: commodity avg `0.0922` n `12`; crypto_alt avg `0.3074` n `229`; crypto_major avg `0.6052` n `8`; equity avg `0.6067` n `88`; fx avg `-0.1289` n `6`; index avg `0.2143` n `25`; metal avg `-0.0928` n `20`; unknown avg `-0.2069` n `745`
- 24h: commodity avg `0.4609` n `12`; crypto_alt avg `2.2919` n `228`; crypto_major avg `3.1833` n `8`; equity avg `0.2458` n `88`; fx avg `-0.2002` n `6`; index avg `0.1981` n `25`; metal avg `1.1236` n `20`; unknown avg `5.6224` n `743`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
