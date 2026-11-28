# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T03:52:27.203442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `0.0002` n `239`; crypto_major avg `-0.0304` n `8`; equity avg `-0.028` n `168`; fx avg `0.0089` n `6`; index avg `0.0003` n `27`; metal avg `-0.0031` n `20`; unknown avg `0.5013` n `1263`
- 1h: commodity avg `-0.009` n `13`; crypto_alt avg `-0.0716` n `239`; crypto_major avg `-0.0552` n `8`; equity avg `-0.0002` n `168`; fx avg `0.0233` n `6`; index avg `0.002` n `27`; metal avg `-0.0343` n `20`; unknown avg `0.7607` n `1257`
- 4h: commodity avg `-0.0623` n `13`; crypto_alt avg `-0.6264` n `239`; crypto_major avg `0.2518` n `8`; equity avg `0.1506` n `168`; fx avg `0.0211` n `6`; index avg `0.0269` n `27`; metal avg `0.0138` n `20`; unknown avg `0.9659` n `1247`
- 24h: commodity avg `-0.7348` n `13`; crypto_alt avg `-1.5072` n `239`; crypto_major avg `-1.6092` n `8`; equity avg `0.8324` n `168`; fx avg `-0.1437` n `6`; index avg `0.0782` n `27`; metal avg `0.1083` n `20`; unknown avg `211.8315` n `985`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
