# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T08:37:27.563074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-5.0026` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.9002` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.8684` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-4.4406` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `-2.0046` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-1.9893` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.9848` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.8257` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `-1.2172` n `230`; crypto_major avg `-1.2567` n `8`; equity avg `-0.0694` n `121`; fx avg `0.0051` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0118` n `20`; unknown avg `-0.2403` n `794`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `-1.4394` n `230`; crypto_major avg `-2.0032` n `8`; equity avg `-0.1775` n `121`; fx avg `0.0052` n `6`; index avg `-0.0184` n `25`; metal avg `-0.0139` n `20`; unknown avg `-0.0776` n `794`
- 4h: commodity avg `0.0564` n `12`; crypto_alt avg `-5.7822` n `230`; crypto_major avg `-4.9462` n `8`; equity avg `-0.5056` n `121`; fx avg `-0.0139` n `6`; index avg `-0.046` n `25`; metal avg `-0.0778` n `20`; unknown avg `-0.2583` n `778`
- 24h: commodity avg `0.1426` n `12`; crypto_alt avg `2.8615` n `230`; crypto_major avg `3.0759` n `8`; equity avg `-0.7622` n `121`; fx avg `0.0777` n `6`; index avg `-0.1036` n `25`; metal avg `-0.2675` n `20`; unknown avg `1.5093` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
