# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T11:37:25.057907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0238` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9971` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7866` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.6342` n `230`; crypto_major avg `0.5562` n `8`; equity avg `0.0358` n `121`; fx avg `0.0009` n `6`; index avg `-0.0005` n `25`; metal avg `0.0179` n `20`; unknown avg `0.1052` n `794`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `0.1727` n `230`; crypto_major avg `0.0044` n `8`; equity avg `-0.0317` n `121`; fx avg `0.0104` n `6`; index avg `0.0036` n `25`; metal avg `-0.0098` n `20`; unknown avg `0.0279` n `794`
- 4h: commodity avg `-0.0288` n `12`; crypto_alt avg `-1.5728` n `230`; crypto_major avg `-2.0224` n `8`; equity avg `-0.2358` n `121`; fx avg `0.0369` n `6`; index avg `-0.0253` n `25`; metal avg `0.0014` n `20`; unknown avg `0.0962` n `794`
- 24h: commodity avg `0.1017` n `12`; crypto_alt avg `2.1585` n `230`; crypto_major avg `3.731` n `8`; equity avg `-1.06` n `121`; fx avg `0.0776` n `6`; index avg `-0.1573` n `25`; metal avg `-0.2348` n `20`; unknown avg `1.4419` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
