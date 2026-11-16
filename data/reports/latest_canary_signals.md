# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T05:07:24.317709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.0949` n `239`; crypto_major avg `-0.0639` n `8`; equity avg `-0.1145` n `162`; fx avg `-0.0122` n `6`; index avg `-0.0117` n `27`; metal avg `-0.0051` n `20`; unknown avg `4.8778` n `1259`
- 1h: commodity avg `-0.0492` n `13`; crypto_alt avg `-0.023` n `239`; crypto_major avg `-0.1508` n `8`; equity avg `-0.2672` n `162`; fx avg `-0.0101` n `6`; index avg `-0.0281` n `27`; metal avg `-0.0294` n `20`; unknown avg `0.8133` n `1259`
- 4h: commodity avg `-0.0224` n `13`; crypto_alt avg `-0.067` n `239`; crypto_major avg `-0.4271` n `8`; equity avg `-1.277` n `162`; fx avg `-0.0309` n `6`; index avg `-0.168` n `27`; metal avg `-0.3327` n `20`; unknown avg `0.7134` n `1243`
- 24h: commodity avg `-0.3593` n `13`; crypto_alt avg `-0.1352` n `239`; crypto_major avg `0.0773` n `8`; equity avg `-0.254` n `162`; fx avg `-0.0514` n `6`; index avg `-0.0273` n `27`; metal avg `0.1559` n `20`; unknown avg `0.3885` n `1131`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
