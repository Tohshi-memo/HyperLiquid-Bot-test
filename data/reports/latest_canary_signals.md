# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T06:22:29.884236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `13`; crypto_alt avg `0.0696` n `234`; crypto_major avg `-0.0173` n `8`; equity avg `-0.0105` n `142`; fx avg `-0.0069` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0362` n `20`; unknown avg `-0.02` n `974`
- 1h: commodity avg `-0.0367` n `13`; crypto_alt avg `0.1078` n `234`; crypto_major avg `0.1159` n `8`; equity avg `0.2084` n `142`; fx avg `-0.0022` n `6`; index avg `0.0246` n `26`; metal avg `0.0215` n `20`; unknown avg `-0.1901` n `946`
- 4h: commodity avg `-0.4007` n `13`; crypto_alt avg `1.4016` n `234`; crypto_major avg `0.8813` n `8`; equity avg `1.0433` n `142`; fx avg `-0.0218` n `6`; index avg `0.2151` n `26`; metal avg `0.2379` n `20`; unknown avg `0.658` n `940`
- 24h: commodity avg `-0.2344` n `13`; crypto_alt avg `1.612` n `234`; crypto_major avg `1.6321` n `8`; equity avg `1.2508` n `142`; fx avg `0.1401` n `6`; index avg `0.3054` n `26`; metal avg `0.0355` n `20`; unknown avg `774.0982` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
