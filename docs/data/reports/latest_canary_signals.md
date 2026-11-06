# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T19:22:25.497972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.128` n `13`; crypto_alt avg `-0.1059` n `239`; crypto_major avg `-0.104` n `8`; equity avg `-0.103` n `158`; fx avg `0.0004` n `6`; index avg `-0.0252` n `27`; metal avg `-0.0557` n `20`; unknown avg `1.5006` n `1261`
- 1h: commodity avg `0.2114` n `13`; crypto_alt avg `-0.1058` n `239`; crypto_major avg `-0.0683` n `8`; equity avg `0.5437` n `158`; fx avg `0.0149` n `6`; index avg `0.0434` n `27`; metal avg `0.0308` n `20`; unknown avg `1.3531` n `1255`
- 4h: commodity avg `0.271` n `13`; crypto_alt avg `-0.6254` n `239`; crypto_major avg `-0.2938` n `8`; equity avg `-0.2795` n `158`; fx avg `-0.009` n `6`; index avg `-0.0838` n `27`; metal avg `-0.0172` n `20`; unknown avg `29.6243` n `1245`
- 24h: commodity avg `0.2489` n `13`; crypto_alt avg `1.2848` n `239`; crypto_major avg `-0.4684` n `8`; equity avg `1.7116` n `158`; fx avg `-0.0895` n `6`; index avg `0.1753` n `27`; metal avg `-0.1741` n `20`; unknown avg `45.1138` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
