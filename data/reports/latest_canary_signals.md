# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T19:52:49.457295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0975` n `13`; crypto_alt avg `0.2618` n `239`; crypto_major avg `0.2023` n `8`; equity avg `-0.1703` n `163`; fx avg `0.0051` n `6`; index avg `-0.031` n `27`; metal avg `-0.0357` n `20`; unknown avg `1.1926` n `1265`
- 1h: commodity avg `-0.288` n `13`; crypto_alt avg `0.2451` n `239`; crypto_major avg `0.0995` n `8`; equity avg `-0.1103` n `163`; fx avg `0.0024` n `6`; index avg `-0.0318` n `27`; metal avg `-0.0824` n `20`; unknown avg `322.7147` n `1263`
- 4h: commodity avg `-0.0913` n `13`; crypto_alt avg `0.9572` n `239`; crypto_major avg `1.3372` n `8`; equity avg `1.5188` n `163`; fx avg `0.0191` n `6`; index avg `0.1377` n `27`; metal avg `-0.1282` n `20`; unknown avg `8.2735` n `1247`
- 24h: commodity avg `0.0516` n `13`; crypto_alt avg `-0.4943` n `239`; crypto_major avg `-0.246` n `8`; equity avg `-2.1869` n `163`; fx avg `0.0327` n `6`; index avg `-0.2503` n `27`; metal avg `-0.1356` n `20`; unknown avg `9.9948` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
