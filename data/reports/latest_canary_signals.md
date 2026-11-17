# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T19:56:06.553914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1142` n `13`; crypto_alt avg `0.299` n `239`; crypto_major avg `0.2077` n `8`; equity avg `-0.2189` n `163`; fx avg `0.0032` n `6`; index avg `-0.0426` n `27`; metal avg `-0.0434` n `20`; unknown avg `1.0257` n `1263`
- 1h: commodity avg `-0.3046` n `13`; crypto_alt avg `0.2823` n `239`; crypto_major avg `0.1049` n `8`; equity avg `-0.159` n `163`; fx avg `0.0005` n `6`; index avg `-0.0434` n `27`; metal avg `-0.09` n `20`; unknown avg `164.9309` n `1261`
- 4h: commodity avg `-0.108` n `13`; crypto_alt avg `0.9947` n `239`; crypto_major avg `1.3428` n `8`; equity avg `1.4695` n `163`; fx avg `0.0172` n `6`; index avg `0.126` n `27`; metal avg `-0.1358` n `20`; unknown avg `8.355` n `1247`
- 24h: commodity avg `0.0349` n `13`; crypto_alt avg `-0.4574` n `239`; crypto_major avg `-0.2405` n `8`; equity avg `-2.2338` n `163`; fx avg `0.0308` n `6`; index avg `-0.2617` n `27`; metal avg `-0.1432` n `20`; unknown avg `10.0907` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
