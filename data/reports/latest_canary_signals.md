# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T19:52:28.613597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `-0.1048` n `235`; crypto_major avg `-0.0873` n `8`; equity avg `0.0039` n `150`; fx avg `0.0006` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0008` n `20`; unknown avg `2.3962` n `1117`
- 1h: commodity avg `0.0278` n `13`; crypto_alt avg `0.0673` n `235`; crypto_major avg `0.0566` n `8`; equity avg `0.035` n `150`; fx avg `0.0002` n `6`; index avg `0.0002` n `26`; metal avg `0.0044` n `20`; unknown avg `0.1432` n `1067`
- 4h: commodity avg `0.0056` n `13`; crypto_alt avg `0.2711` n `235`; crypto_major avg `-0.1345` n `8`; equity avg `-0.0117` n `150`; fx avg `-0.0038` n `6`; index avg `-0.0196` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.0126` n `1007`
- 24h: commodity avg `-0.143` n `13`; crypto_alt avg `3.5551` n `235`; crypto_major avg `1.4983` n `8`; equity avg `0.2979` n `150`; fx avg `0.0029` n `6`; index avg `0.0271` n `26`; metal avg `0.005` n `20`; unknown avg `0.14` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
