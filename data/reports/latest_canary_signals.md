# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T10:37:19.403590+00:00`
- Correlation status: `ready`
- Asset price records: `638`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1881` n `12`; crypto_alt avg `0.2428` n `228`; crypto_major avg `0.2417` n `8`; equity avg `0.0342` n `65`; fx avg `-0.01` n `5`; index avg `-0.0672` n `23`; metal avg `0.1815` n `18`; unknown avg `0.0219` n `375`
- 1h: commodity avg `0.0941` n `12`; crypto_alt avg `0.0577` n `228`; crypto_major avg `0.0379` n `8`; equity avg `-0.0494` n `65`; fx avg `0.0285` n `5`; index avg `-0.0614` n `23`; metal avg `0.1939` n `18`; unknown avg `0.0103` n `375`
- 4h: commodity avg `0.2411` n `12`; crypto_alt avg `0.8164` n `228`; crypto_major avg `0.6949` n `8`; equity avg `0.6285` n `65`; fx avg `0.028` n `5`; index avg `0.0753` n `23`; metal avg `-0.0612` n `18`; unknown avg `0.5376` n `375`
- 24h: commodity avg `0.8884` n `12`; crypto_alt avg `1.4573` n `228`; crypto_major avg `-1.0626` n `8`; equity avg `-0.4075` n `65`; fx avg `0.25` n `5`; index avg `-0.4399` n `23`; metal avg `-0.2179` n `18`; unknown avg `0.0117` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1426`, n `630`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1409`, n `630`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `634`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `634`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `634`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `634`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `630`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0833`, n `630`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `630`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `634`, weak_sample_signal
