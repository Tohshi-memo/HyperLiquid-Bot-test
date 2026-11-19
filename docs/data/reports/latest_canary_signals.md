# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T10:37:39.881079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0587` n `13`; crypto_alt avg `-0.0913` n `239`; crypto_major avg `-0.0897` n `8`; equity avg `0.0257` n `164`; fx avg `0.0355` n `6`; index avg `-0.0316` n `27`; metal avg `-0.0315` n `20`; unknown avg `8.1068` n `1266`
- 1h: commodity avg `0.2666` n `13`; crypto_alt avg `-0.2251` n `239`; crypto_major avg `-0.1696` n `8`; equity avg `0.327` n `164`; fx avg `0.0301` n `6`; index avg `0.0954` n `27`; metal avg `-0.0433` n `20`; unknown avg `234.3507` n `1264`
- 4h: commodity avg `0.0921` n `13`; crypto_alt avg `0.1686` n `239`; crypto_major avg `0.0498` n `8`; equity avg `0.8397` n `164`; fx avg `0.1241` n `6`; index avg `0.1606` n `27`; metal avg `-0.0172` n `20`; unknown avg `300.9724` n `1222`
- 24h: commodity avg `0.2713` n `13`; crypto_alt avg `0.0072` n `239`; crypto_major avg `-0.3493` n `8`; equity avg `0.4035` n `164`; fx avg `0.0687` n `6`; index avg `0.2189` n `27`; metal avg `-0.2026` n `20`; unknown avg `4.0086` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
