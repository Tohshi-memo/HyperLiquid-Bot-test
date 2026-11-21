# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T12:07:22.521517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `13`; crypto_alt avg `-0.0636` n `239`; crypto_major avg `0.0219` n `8`; equity avg `-0.0638` n `166`; fx avg `0.0023` n `6`; index avg `-0.0054` n `27`; metal avg `-0.0042` n `20`; unknown avg `146.4907` n `1246`
- 1h: commodity avg `0.0263` n `13`; crypto_alt avg `0.3911` n `239`; crypto_major avg `0.684` n `8`; equity avg `0.0975` n `166`; fx avg `0.0045` n `6`; index avg `0.0017` n `27`; metal avg `-0.0014` n `20`; unknown avg `2.1929` n `1222`
- 4h: commodity avg `0.0349` n `13`; crypto_alt avg `0.7063` n `239`; crypto_major avg `1.3703` n `8`; equity avg `0.0547` n `166`; fx avg `0.0426` n `6`; index avg `0.0032` n `27`; metal avg `0.0529` n `20`; unknown avg `2.3797` n `1220`
- 24h: commodity avg `0.5314` n `13`; crypto_alt avg `-4.0475` n `239`; crypto_major avg `-4.2459` n `8`; equity avg `-3.7026` n `166`; fx avg `-0.0731` n `6`; index avg `-0.4328` n `27`; metal avg `-0.3382` n `20`; unknown avg `2.5547` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
