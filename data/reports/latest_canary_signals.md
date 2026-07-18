# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T00:37:28.124653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.0188` n `230`; crypto_major avg `-0.1197` n `8`; equity avg `0.0059` n `96`; fx avg `0.0` n `6`; index avg `-0.0076` n `25`; metal avg `0.0033` n `20`; unknown avg `0.1206` n `769`
- 1h: commodity avg `-0.0922` n `12`; crypto_alt avg `0.0025` n `230`; crypto_major avg `-0.0774` n `8`; equity avg `0.0629` n `96`; fx avg `-0.0031` n `6`; index avg `0.0223` n `25`; metal avg `0.0478` n `20`; unknown avg `-0.0675` n `769`
- 4h: commodity avg `0.0014` n `12`; crypto_alt avg `0.1537` n `230`; crypto_major avg `0.0116` n `8`; equity avg `0.0523` n `96`; fx avg `-0.0221` n `6`; index avg `0.003` n `25`; metal avg `0.0923` n `20`; unknown avg `-0.1382` n `769`
- 24h: commodity avg `0.6472` n `12`; crypto_alt avg `-0.0` n `230`; crypto_major avg `-0.2044` n `8`; equity avg `-0.1038` n `94`; fx avg `0.0306` n `6`; index avg `-0.1145` n `25`; metal avg `0.1304` n `20`; unknown avg `0.1781` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
