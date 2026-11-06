# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T15:22:29.019534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0472` n `13`; crypto_alt avg `0.2387` n `239`; crypto_major avg `0.4049` n `8`; equity avg `0.0941` n `158`; fx avg `0.0089` n `6`; index avg `0.0281` n `27`; metal avg `0.1234` n `20`; unknown avg `0.5488` n `1255`
- 1h: commodity avg `-0.1011` n `13`; crypto_alt avg `0.6318` n `239`; crypto_major avg `0.3434` n `8`; equity avg `-0.6617` n `158`; fx avg `0.0167` n `6`; index avg `0.0514` n `27`; metal avg `0.2344` n `20`; unknown avg `0.6114` n `1251`
- 4h: commodity avg `-0.3218` n `13`; crypto_alt avg `0.5421` n `239`; crypto_major avg `0.0356` n `8`; equity avg `-0.2974` n `158`; fx avg `0.0003` n `6`; index avg `0.0766` n `27`; metal avg `0.071` n `20`; unknown avg `62.2758` n `1189`
- 24h: commodity avg `0.1174` n `13`; crypto_alt avg `1.8533` n `239`; crypto_major avg `-1.1558` n `8`; equity avg `0.9302` n `158`; fx avg `-0.0693` n `6`; index avg `-0.0233` n `27`; metal avg `-0.2058` n `20`; unknown avg `37.5538` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
