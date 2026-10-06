# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T15:22:33.636087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `13`; crypto_alt avg `0.0476` n `235`; crypto_major avg `-0.0156` n `8`; equity avg `-0.0523` n `150`; fx avg `0.0146` n `6`; index avg `0.0032` n `26`; metal avg `0.042` n `20`; unknown avg `0.2928` n `1076`
- 1h: commodity avg `-0.0316` n `13`; crypto_alt avg `0.5113` n `235`; crypto_major avg `0.3091` n `8`; equity avg `0.1524` n `150`; fx avg `0.0284` n `6`; index avg `0.0303` n `26`; metal avg `0.1727` n `20`; unknown avg `0.1882` n `1046`
- 4h: commodity avg `0.1439` n `13`; crypto_alt avg `0.1575` n `235`; crypto_major avg `0.2657` n `8`; equity avg `0.4312` n `150`; fx avg `0.0135` n `6`; index avg `0.0251` n `26`; metal avg `-0.0447` n `20`; unknown avg `4.678` n `1018`
- 24h: commodity avg `-0.6832` n `13`; crypto_alt avg `0.7583` n `235`; crypto_major avg `0.7815` n `8`; equity avg `1.1556` n `149`; fx avg `0.1118` n `6`; index avg `0.2011` n `26`; metal avg `0.0538` n `20`; unknown avg `381.1233` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
