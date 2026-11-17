# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T13:07:29.721382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0581` n `13`; crypto_alt avg `0.1265` n `239`; crypto_major avg `0.1939` n `8`; equity avg `0.1184` n `162`; fx avg `-0.0078` n `6`; index avg `0.009` n `27`; metal avg `0.0113` n `20`; unknown avg `5.2804` n `1260`
- 1h: commodity avg `0.089` n `13`; crypto_alt avg `0.4619` n `239`; crypto_major avg `0.534` n `8`; equity avg `0.1372` n `162`; fx avg `0.0102` n `6`; index avg `0.0192` n `27`; metal avg `-0.0243` n `20`; unknown avg `0.0032` n `1260`
- 4h: commodity avg `0.2409` n `13`; crypto_alt avg `1.2464` n `239`; crypto_major avg `1.1908` n `8`; equity avg `1.5498` n `162`; fx avg `0.0221` n `6`; index avg `0.1369` n `27`; metal avg `0.0672` n `20`; unknown avg `0.8408` n `1254`
- 24h: commodity avg `-0.4678` n `13`; crypto_alt avg `2.4294` n `239`; crypto_major avg `2.4015` n `8`; equity avg `-0.8863` n `162`; fx avg `-0.0471` n `6`; index avg `-0.131` n `27`; metal avg `-0.1464` n `20`; unknown avg `190.586` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
