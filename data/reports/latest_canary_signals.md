# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T06:37:33.089837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `13`; crypto_alt avg `-0.3315` n `239`; crypto_major avg `-0.4147` n `8`; equity avg `-0.1951` n `162`; fx avg `-0.0101` n `6`; index avg `-0.0025` n `27`; metal avg `0.0259` n `20`; unknown avg `0.0488` n `1264`
- 1h: commodity avg `0.0988` n `13`; crypto_alt avg `-0.7844` n `239`; crypto_major avg `-0.8708` n `8`; equity avg `-0.7095` n `162`; fx avg `0.0023` n `6`; index avg `-0.0349` n `27`; metal avg `-0.1291` n `20`; unknown avg `-0.0707` n `1246`
- 4h: commodity avg `0.0339` n `13`; crypto_alt avg `0.0813` n `239`; crypto_major avg `0.1282` n `8`; equity avg `-0.737` n `162`; fx avg `-0.0129` n `6`; index avg `-0.0823` n `27`; metal avg `0.0293` n `20`; unknown avg `-0.3825` n `1218`
- 24h: commodity avg `-1.2594` n `13`; crypto_alt avg `0.4337` n `239`; crypto_major avg `0.7674` n `8`; equity avg `-2.7529` n `162`; fx avg `-0.0398` n `6`; index avg `-0.2486` n `27`; metal avg `0.0459` n `20`; unknown avg `567.8601` n `981`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
