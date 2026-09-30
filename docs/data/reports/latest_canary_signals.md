# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T00:22:31.793338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0381` n `12`; crypto_alt avg `-0.4731` n `234`; crypto_major avg `-0.3323` n `8`; equity avg `-0.1403` n `142`; fx avg `0.0154` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0298` n `20`; unknown avg `0.7976` n `963`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.8704` n `234`; crypto_major avg `-0.5312` n `8`; equity avg `-0.0015` n `142`; fx avg `0.0052` n `6`; index avg `0.0173` n `26`; metal avg `-0.0209` n `20`; unknown avg `1.1823` n `955`
- 4h: commodity avg `0.0602` n `12`; crypto_alt avg `-1.0001` n `234`; crypto_major avg `-0.3888` n `8`; equity avg `0.1487` n `142`; fx avg `0.0076` n `6`; index avg `0.0449` n `26`; metal avg `0.0472` n `20`; unknown avg `1.6797` n `902`
- 24h: commodity avg `-0.8528` n `12`; crypto_alt avg `-0.3682` n `234`; crypto_major avg `-0.4655` n `8`; equity avg `0.8209` n `142`; fx avg `-0.1534` n `6`; index avg `0.1321` n `26`; metal avg `0.2979` n `20`; unknown avg `3099.1268` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
