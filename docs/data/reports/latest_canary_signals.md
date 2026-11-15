# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T06:37:25.097624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `0.0655` n `239`; crypto_major avg `-0.0921` n `8`; equity avg `-0.0183` n `162`; fx avg `-0.002` n `6`; index avg `0.0011` n `27`; metal avg `-0.0014` n `20`; unknown avg `-0.0492` n `1261`
- 1h: commodity avg `-0.0108` n `13`; crypto_alt avg `-0.0893` n `239`; crypto_major avg `-0.5931` n `8`; equity avg `-0.1741` n `162`; fx avg `-0.0005` n `6`; index avg `-0.0161` n `27`; metal avg `-0.0201` n `20`; unknown avg `-0.051` n `1241`
- 4h: commodity avg `0.0248` n `13`; crypto_alt avg `0.1111` n `239`; crypto_major avg `-0.4339` n `8`; equity avg `-0.0932` n `162`; fx avg `0.0122` n `6`; index avg `-0.02` n `27`; metal avg `-0.0178` n `20`; unknown avg `0.5262` n `1225`
- 24h: commodity avg `0.0515` n `13`; crypto_alt avg `-5.553` n `239`; crypto_major avg `-4.9812` n `8`; equity avg `-1.0671` n `162`; fx avg `0.0398` n `6`; index avg `-0.1006` n `27`; metal avg `-0.4827` n `20`; unknown avg `46.8197` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
