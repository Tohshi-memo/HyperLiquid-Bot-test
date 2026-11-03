# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T06:07:32.859076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `13`; crypto_alt avg `-0.1536` n `239`; crypto_major avg `-0.2181` n `8`; equity avg `-0.1771` n `157`; fx avg `-0.0135` n `6`; index avg `-0.0091` n `27`; metal avg `-0.0059` n `20`; unknown avg `4.2171` n `1242`
- 1h: commodity avg `0.0499` n `13`; crypto_alt avg `-0.2362` n `239`; crypto_major avg `-0.3126` n `8`; equity avg `-0.2791` n `157`; fx avg `0.0064` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0948` n `20`; unknown avg `0.6976` n `1238`
- 4h: commodity avg `0.2492` n `13`; crypto_alt avg `-0.297` n `239`; crypto_major avg `-0.423` n `8`; equity avg `-1.2514` n `157`; fx avg `0.0103` n `6`; index avg `-0.1144` n `27`; metal avg `-0.3834` n `20`; unknown avg `0.3266` n `1172`
- 24h: commodity avg `-0.8052` n `13`; crypto_alt avg `-3.0531` n `238`; crypto_major avg `-2.307` n `8`; equity avg `-4.7763` n `157`; fx avg `0.0286` n `6`; index avg `-0.3701` n `27`; metal avg `-0.3967` n `20`; unknown avg `8.5114` n `955`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
