# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T11:07:24.879012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `13`; crypto_alt avg `-0.1588` n `239`; crypto_major avg `-0.0932` n `8`; equity avg `-0.0062` n `166`; fx avg `0.0133` n `6`; index avg `-0.0` n `27`; metal avg `-0.0057` n `20`; unknown avg `0.1358` n `1252`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.095` n `239`; crypto_major avg `0.212` n `8`; equity avg `-0.0588` n `166`; fx avg `-0.0041` n `6`; index avg `-0.0089` n `27`; metal avg `0.0116` n `20`; unknown avg `0.5561` n `1256`
- 4h: commodity avg `-0.0378` n `13`; crypto_alt avg `-0.4796` n `239`; crypto_major avg `-0.3381` n `8`; equity avg `-0.3004` n `166`; fx avg `0.0423` n `6`; index avg `-0.0245` n `27`; metal avg `-0.001` n `20`; unknown avg `162.4029` n `1236`
- 24h: commodity avg `0.5997` n `13`; crypto_alt avg `-5.4882` n `239`; crypto_major avg `-6.1457` n `8`; equity avg `-4.6299` n `166`; fx avg `-0.0744` n `6`; index avg `-0.4939` n `27`; metal avg `-0.5206` n `20`; unknown avg `174.157` n `1149`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
