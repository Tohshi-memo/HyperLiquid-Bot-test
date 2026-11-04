# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T23:22:26.156504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `-0.2012` n `239`; crypto_major avg `-0.1596` n `8`; equity avg `-0.0671` n `158`; fx avg `-0.0075` n `6`; index avg `-0.0064` n `27`; metal avg `-0.0006` n `20`; unknown avg `158.3656` n `1262`
- 1h: commodity avg `0.0481` n `13`; crypto_alt avg `-0.2232` n `239`; crypto_major avg `-0.1058` n `8`; equity avg `-0.3219` n `158`; fx avg `0.0198` n `6`; index avg `-0.002` n `27`; metal avg `0.0115` n `20`; unknown avg `-0.0152` n `1202`
- 4h: commodity avg `0.1262` n `13`; crypto_alt avg `0.4067` n `239`; crypto_major avg `0.1142` n `8`; equity avg `0.0852` n `158`; fx avg `0.0262` n `6`; index avg `0.0332` n `27`; metal avg `-0.0001` n `20`; unknown avg `175.794` n `1138`
- 24h: commodity avg `-1.8236` n `13`; crypto_alt avg `1.5307` n `239`; crypto_major avg `1.9556` n `8`; equity avg `-1.8883` n `158`; fx avg `0.0823` n `6`; index avg `0.0424` n `27`; metal avg `1.2246` n `20`; unknown avg `29.7048` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2662`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
