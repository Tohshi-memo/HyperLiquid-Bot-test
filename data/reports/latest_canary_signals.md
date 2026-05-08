# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T15:52:19.614830+00:00`
- Correlation status: `ready`
- Asset price records: `659`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1702` n `12`; crypto_alt avg `0.3078` n `228`; crypto_major avg `0.3418` n `8`; equity avg `-0.1828` n `65`; fx avg `0.0167` n `5`; index avg `-0.0584` n `23`; metal avg `-0.0556` n `18`; unknown avg `0.0126` n `375`
- 1h: commodity avg `0.1688` n `12`; crypto_alt avg `0.0765` n `228`; crypto_major avg `0.0837` n `8`; equity avg `0.0078` n `65`; fx avg `-0.0077` n `5`; index avg `-0.0077` n `23`; metal avg `-0.3682` n `18`; unknown avg `-0.0207` n `375`
- 4h: commodity avg `0.5739` n `12`; crypto_alt avg `0.5966` n `228`; crypto_major avg `0.2373` n `8`; equity avg `0.9342` n `65`; fx avg `-0.049` n `5`; index avg `0.4296` n `23`; metal avg `-0.3526` n `18`; unknown avg `0.0881` n `375`
- 24h: commodity avg `1.4299` n `12`; crypto_alt avg `2.6672` n `228`; crypto_major avg `0.2734` n `8`; equity avg `1.2858` n `65`; fx avg `0.1704` n `5`; index avg `0.4751` n `23`; metal avg `-0.4077` n `18`; unknown avg `0.1209` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1209`, n `651`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1168`, n `651`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1162`, n `655`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `651`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `655`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0966`, n `651`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `655`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `655`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `655`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `655`, weak_sample_signal
