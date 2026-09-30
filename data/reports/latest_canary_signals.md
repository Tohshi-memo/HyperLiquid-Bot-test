# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T05:22:31.204671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.0224` n `234`; crypto_major avg `-0.0243` n `8`; equity avg `-0.1139` n `142`; fx avg `-0.019` n `6`; index avg `-0.0216` n `26`; metal avg `-0.0351` n `20`; unknown avg `2.3979` n `963`
- 1h: commodity avg `0.0671` n `12`; crypto_alt avg `-0.1264` n `234`; crypto_major avg `-0.2001` n `8`; equity avg `-0.1442` n `142`; fx avg `-0.0024` n `6`; index avg `-0.0311` n `26`; metal avg `-0.0392` n `20`; unknown avg `1.1005` n `961`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `-0.2529` n `234`; crypto_major avg `-0.2009` n `8`; equity avg `-0.2868` n `142`; fx avg `-0.0159` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0552` n `20`; unknown avg `5.4166` n `955`
- 24h: commodity avg `-0.944` n `12`; crypto_alt avg `1.4915` n `234`; crypto_major avg `-0.011` n `8`; equity avg `0.9728` n `142`; fx avg `-0.123` n `6`; index avg `0.1721` n `26`; metal avg `0.1896` n `20`; unknown avg `3240.911` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
