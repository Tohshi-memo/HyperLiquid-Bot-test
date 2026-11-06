# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T11:07:40.686841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0347` n `13`; crypto_alt avg `0.0189` n `239`; crypto_major avg `-0.0594` n `8`; equity avg `-0.0912` n `158`; fx avg `-0.0014` n `6`; index avg `-0.0277` n `27`; metal avg `-0.0131` n `20`; unknown avg `0.1192` n `1241`
- 1h: commodity avg `0.2231` n `13`; crypto_alt avg `0.0697` n `239`; crypto_major avg `0.0266` n `8`; equity avg `-0.13` n `158`; fx avg `0.0341` n `6`; index avg `-0.0265` n `27`; metal avg `-0.0776` n `20`; unknown avg `0.2996` n `1242`
- 4h: commodity avg `-0.1039` n `13`; crypto_alt avg `0.9834` n `239`; crypto_major avg `0.8301` n `8`; equity avg `1.4794` n `158`; fx avg `-0.014` n `6`; index avg `0.2011` n `27`; metal avg `0.1324` n `20`; unknown avg `1.1622` n `1184`
- 24h: commodity avg `0.8198` n `13`; crypto_alt avg `-3.1662` n `239`; crypto_major avg `-5.3277` n `8`; equity avg `-4.8767` n `158`; fx avg `-0.0237` n `6`; index avg `-0.6604` n `27`; metal avg `-0.4274` n `20`; unknown avg `10.7443` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
