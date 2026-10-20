# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T01:07:26.970851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0832` n `13`; crypto_alt avg `-0.2923` n `237`; crypto_major avg `-0.2766` n `8`; equity avg `-0.0714` n `151`; fx avg `0.0236` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0281` n `20`; unknown avg `-0.2672` n `1196`
- 1h: commodity avg `0.1201` n `13`; crypto_alt avg `-0.4068` n `237`; crypto_major avg `-0.4417` n `8`; equity avg `-0.4638` n `151`; fx avg `0.0084` n `6`; index avg `-0.1093` n `26`; metal avg `-0.0979` n `20`; unknown avg `-0.2584` n `1196`
- 4h: commodity avg `0.0834` n `13`; crypto_alt avg `0.1104` n `237`; crypto_major avg `-0.2506` n `8`; equity avg `-0.9581` n `151`; fx avg `-0.039` n `6`; index avg `-0.1737` n `26`; metal avg `-0.1359` n `20`; unknown avg `3.3059` n `1178`
- 24h: commodity avg `0.1852` n `13`; crypto_alt avg `-0.2671` n `237`; crypto_major avg `-0.5715` n `8`; equity avg `-0.5937` n `151`; fx avg `-0.0723` n `6`; index avg `-0.0534` n `26`; metal avg `-0.284` n `20`; unknown avg `5.1449` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
