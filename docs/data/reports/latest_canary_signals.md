# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T04:22:24.969763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0282` n `13`; crypto_alt avg `-0.1914` n `239`; crypto_major avg `-0.039` n `8`; equity avg `-0.0759` n `164`; fx avg `0.0142` n `6`; index avg `0.0013` n `27`; metal avg `0.0005` n `20`; unknown avg `2.1774` n `1262`
- 1h: commodity avg `0.0582` n `13`; crypto_alt avg `0.8886` n `239`; crypto_major avg `1.1543` n `8`; equity avg `0.8986` n `164`; fx avg `0.021` n `6`; index avg `0.148` n `27`; metal avg `0.221` n `20`; unknown avg `14.4155` n `1243`
- 4h: commodity avg `0.0512` n `13`; crypto_alt avg `1.1193` n `239`; crypto_major avg `1.1944` n `8`; equity avg `0.5967` n `164`; fx avg `0.0204` n `6`; index avg `0.1132` n `27`; metal avg `-0.1133` n `20`; unknown avg `15.2485` n `1243`
- 24h: commodity avg `0.0617` n `13`; crypto_alt avg `0.4352` n `239`; crypto_major avg `-0.7698` n `8`; equity avg `-0.2369` n `164`; fx avg `-0.0961` n `6`; index avg `0.0827` n `27`; metal avg `-0.5564` n `20`; unknown avg `128.4429` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
