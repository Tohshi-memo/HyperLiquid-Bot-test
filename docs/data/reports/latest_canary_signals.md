# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T14:22:35.495625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `0.0907` n `239`; crypto_major avg `0.1139` n `8`; equity avg `0.0261` n `162`; fx avg `-0.0021` n `6`; index avg `0.0077` n `27`; metal avg `0.0084` n `20`; unknown avg `0.0639` n `1262`
- 1h: commodity avg `-0.1014` n `13`; crypto_alt avg `-0.8177` n `239`; crypto_major avg `-0.8085` n `8`; equity avg `-0.1497` n `162`; fx avg `0.0019` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0121` n `20`; unknown avg `-0.0576` n `1262`
- 4h: commodity avg `-0.0969` n `13`; crypto_alt avg `-0.4009` n `239`; crypto_major avg `-0.2165` n `8`; equity avg `-0.0788` n `162`; fx avg `-0.0345` n `6`; index avg `0.0024` n `27`; metal avg `0.0027` n `20`; unknown avg `-0.1399` n `1253`
- 24h: commodity avg `-0.0474` n `13`; crypto_alt avg `-2.1625` n `239`; crypto_major avg `-1.4598` n `8`; equity avg `-0.3847` n `162`; fx avg `-0.0091` n `6`; index avg `-0.0321` n `27`; metal avg `-0.278` n `20`; unknown avg `0.3119` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
