# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T19:22:33.236344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0837` n `13`; crypto_alt avg `0.4587` n `239`; crypto_major avg `0.2862` n `8`; equity avg `0.4976` n `158`; fx avg `-0.0058` n `6`; index avg `0.0372` n `27`; metal avg `0.0253` n `20`; unknown avg `0.3567` n `1256`
- 1h: commodity avg `-0.0191` n `13`; crypto_alt avg `0.7829` n `239`; crypto_major avg `0.1051` n `8`; equity avg `0.3902` n `158`; fx avg `-0.025` n `6`; index avg `0.0047` n `27`; metal avg `0.0277` n `20`; unknown avg `6.9332` n `1254`
- 4h: commodity avg `0.1421` n `13`; crypto_alt avg `-0.0681` n `239`; crypto_major avg `-0.9881` n `8`; equity avg `-1.0514` n `158`; fx avg `0.0113` n `6`; index avg `-0.2797` n `27`; metal avg `-0.0495` n `20`; unknown avg `8.5418` n `1250`
- 24h: commodity avg `0.8944` n `13`; crypto_alt avg `-4.3256` n `239`; crypto_major avg `-5.0831` n `8`; equity avg `-7.6709` n `158`; fx avg `0.1` n `6`; index avg `-1.0609` n `27`; metal avg `0.2396` n `20`; unknown avg `406.3733` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
