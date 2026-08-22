# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T08:22:23.222609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4455` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3459` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3234` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9638` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `-0.4762` n `230`; crypto_major avg `-0.4508` n `8`; equity avg `-0.03` n `121`; fx avg `0.0` n `6`; index avg `0.0021` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0603` n `794`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `-0.2888` n `230`; crypto_major avg `-0.5844` n `8`; equity avg `-0.1003` n `121`; fx avg `-0.0074` n `6`; index avg `-0.0174` n `25`; metal avg `0.0172` n `20`; unknown avg `0.1694` n `794`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `-4.0056` n `230`; crypto_major avg `-2.3877` n `8`; equity avg `-0.4239` n `121`; fx avg `-0.0189` n `6`; index avg `-0.0418` n `25`; metal avg `-0.0643` n `20`; unknown avg `-0.0419` n `778`
- 24h: commodity avg `0.102` n `12`; crypto_alt avg `4.5884` n `230`; crypto_major avg `5.0862` n `8`; equity avg `-0.4064` n `121`; fx avg `0.0564` n `6`; index avg `-0.0603` n `25`; metal avg `-0.1492` n `20`; unknown avg `1.9572` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
