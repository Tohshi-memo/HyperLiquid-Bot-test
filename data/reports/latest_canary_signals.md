# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T05:37:25.902738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0707` n `13`; crypto_alt avg `0.1744` n `239`; crypto_major avg `0.1345` n `8`; equity avg `0.2453` n `158`; fx avg `-0.0088` n `6`; index avg `0.0576` n `27`; metal avg `0.0568` n `20`; unknown avg `88.8172` n `1254`
- 1h: commodity avg `-0.0633` n `13`; crypto_alt avg `-0.2461` n `239`; crypto_major avg `-0.233` n `8`; equity avg `-0.0994` n `158`; fx avg `0.0295` n `6`; index avg `0.017` n `27`; metal avg `-0.011` n `20`; unknown avg `181.1681` n `1250`
- 4h: commodity avg `0.1318` n `13`; crypto_alt avg `0.1621` n `239`; crypto_major avg `-0.5995` n `8`; equity avg `0.5989` n `158`; fx avg `-0.0085` n `6`; index avg `0.166` n `27`; metal avg `-0.2004` n `20`; unknown avg `1.4447` n `1242`
- 24h: commodity avg `1.3134` n `13`; crypto_alt avg `-4.2868` n `239`; crypto_major avg `-5.8401` n `8`; equity avg `-5.7135` n `158`; fx avg `0.0402` n `6`; index avg `-0.6967` n `27`; metal avg `-0.3925` n `20`; unknown avg `230.6804` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.24`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
