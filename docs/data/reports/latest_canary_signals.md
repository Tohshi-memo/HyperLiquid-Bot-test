# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T18:53:59.540225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `-0.0875` n `239`; crypto_major avg `-0.1863` n `8`; equity avg `-0.0814` n `158`; fx avg `-0.0058` n `6`; index avg `-0.0253` n `27`; metal avg `-0.0181` n `20`; unknown avg `0.3097` n `1263`
- 1h: commodity avg `0.027` n `13`; crypto_alt avg `-0.0064` n `239`; crypto_major avg `-0.2168` n `8`; equity avg `-0.0469` n `158`; fx avg `0.0054` n `6`; index avg `-0.0132` n `27`; metal avg `-0.02` n `20`; unknown avg `-0.2602` n `1219`
- 4h: commodity avg `0.1759` n `13`; crypto_alt avg `-0.3238` n `239`; crypto_major avg `-0.1962` n `8`; equity avg `-0.101` n `158`; fx avg `0.0339` n `6`; index avg `-0.0009` n `27`; metal avg `-0.1899` n `20`; unknown avg `-0.2595` n `1215`
- 24h: commodity avg `0.1848` n `13`; crypto_alt avg `1.0559` n `239`; crypto_major avg `1.4652` n `8`; equity avg `0.6699` n `158`; fx avg `0.0837` n `6`; index avg `0.0264` n `27`; metal avg `-0.529` n `20`; unknown avg `373.1941` n `1053`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
