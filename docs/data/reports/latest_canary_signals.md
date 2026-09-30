# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T01:37:40.216159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.1192` n `234`; crypto_major avg `-0.1153` n `8`; equity avg `-0.0277` n `142`; fx avg `0.0152` n `6`; index avg `-0.0127` n `26`; metal avg `-0.025` n `20`; unknown avg `1.7064` n `963`
- 1h: commodity avg `0.0977` n `12`; crypto_alt avg `0.7324` n `234`; crypto_major avg `0.1263` n `8`; equity avg `-0.0968` n `142`; fx avg `-0.0383` n `6`; index avg `-0.0404` n `26`; metal avg `-0.1078` n `20`; unknown avg `1.923` n `961`
- 4h: commodity avg `0.1092` n `12`; crypto_alt avg `0.2258` n `234`; crypto_major avg `0.0856` n `8`; equity avg `-0.0175` n `142`; fx avg `0.0144` n `6`; index avg `-0.0038` n `26`; metal avg `-0.1025` n `20`; unknown avg `0.9586` n `928`
- 24h: commodity avg `-0.9089` n `12`; crypto_alt avg `2.5562` n `234`; crypto_major avg `0.9298` n `8`; equity avg `1.0198` n `142`; fx avg `-0.1455` n `6`; index avg `0.1096` n `26`; metal avg `0.2033` n `20`; unknown avg `3100.4091` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
