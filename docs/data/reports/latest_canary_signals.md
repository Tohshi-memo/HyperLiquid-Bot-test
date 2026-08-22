# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T21:52:27.721112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.5829` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5619` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.5369` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.2508` n `230`; crypto_major avg `-0.1758` n `8`; equity avg `0.0245` n `121`; fx avg `-0.0028` n `6`; index avg `0.0007` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.0141` n `794`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-1.9575` n `230`; crypto_major avg `-1.5645` n `8`; equity avg `-0.0276` n `121`; fx avg `-0.0081` n `6`; index avg `-0.0026` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.1235` n `794`
- 4h: commodity avg `0.0911` n `12`; crypto_alt avg `-2.255` n `230`; crypto_major avg `-0.9786` n `8`; equity avg `0.079` n `121`; fx avg `0.0287` n `6`; index avg `-0.0069` n `25`; metal avg `0.0144` n `20`; unknown avg `0.3388` n `794`
- 24h: commodity avg `0.0785` n `12`; crypto_alt avg `-2.6005` n `230`; crypto_major avg `-0.0255` n `8`; equity avg `-0.4172` n `121`; fx avg `0.0621` n `6`; index avg `-0.0529` n `25`; metal avg `-0.0738` n `20`; unknown avg `3.0703` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
