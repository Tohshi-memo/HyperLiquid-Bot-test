# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T18:07:48.431696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0599` n `13`; crypto_alt avg `-0.0002` n `238`; crypto_major avg `-0.092` n `8`; equity avg `-0.2015` n `155`; fx avg `0.0029` n `6`; index avg `-0.0368` n `27`; metal avg `-0.0212` n `20`; unknown avg `0.7815` n `1232`
- 1h: commodity avg `-0.0513` n `13`; crypto_alt avg `0.1888` n `238`; crypto_major avg `0.2792` n `8`; equity avg `-0.1682` n `155`; fx avg `-0.0157` n `6`; index avg `-0.0586` n `27`; metal avg `-0.0391` n `20`; unknown avg `1.8672` n `1232`
- 4h: commodity avg `0.1004` n `13`; crypto_alt avg `0.0314` n `238`; crypto_major avg `0.1496` n `8`; equity avg `0.1614` n `155`; fx avg `0.0604` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0893` n `20`; unknown avg `1.8148` n `1182`
- 24h: commodity avg `0.5901` n `13`; crypto_alt avg `-0.1423` n `238`; crypto_major avg `0.1272` n `8`; equity avg `1.0574` n `154`; fx avg `0.2508` n `6`; index avg `0.2301` n `27`; metal avg `-0.1808` n `20`; unknown avg `5.1886` n `1100`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
