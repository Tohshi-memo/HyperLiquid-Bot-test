# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T13:22:28.946915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0395` n `13`; crypto_alt avg `-0.1012` n `239`; crypto_major avg `-0.1906` n `8`; equity avg `-0.1853` n `164`; fx avg `-0.0104` n `6`; index avg `-0.0154` n `27`; metal avg `-0.0704` n `20`; unknown avg `9.8585` n `1264`
- 1h: commodity avg `-0.0066` n `13`; crypto_alt avg `0.1827` n `239`; crypto_major avg `0.1726` n `8`; equity avg `-0.0431` n `164`; fx avg `0.0007` n `6`; index avg `-0.0098` n `27`; metal avg `-0.0266` n `20`; unknown avg `12.493` n `1264`
- 4h: commodity avg `0.1302` n `13`; crypto_alt avg `0.0478` n `239`; crypto_major avg `0.1467` n `8`; equity avg `0.2281` n `164`; fx avg `-0.0317` n `6`; index avg `0.0765` n `27`; metal avg `-0.1461` n `20`; unknown avg `12.344` n `1258`
- 24h: commodity avg `-0.0123` n `13`; crypto_alt avg `0.408` n `239`; crypto_major avg `0.354` n `8`; equity avg `1.2312` n `164`; fx avg `0.0073` n `6`; index avg `0.3329` n `27`; metal avg `-0.2755` n `20`; unknown avg `3.6474` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
