# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T20:07:30.036596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0834` n `12`; crypto_alt avg `0.0412` n `234`; crypto_major avg `0.0` n `8`; equity avg `-0.1484` n `140`; fx avg `-0.0067` n `6`; index avg `-0.0342` n `26`; metal avg `-0.0647` n `20`; unknown avg `49.1383` n `934`
- 1h: commodity avg `-0.0674` n `12`; crypto_alt avg `0.0646` n `234`; crypto_major avg `-0.2839` n `8`; equity avg `0.0318` n `140`; fx avg `-0.0202` n `6`; index avg `0.0184` n `26`; metal avg `0.0292` n `20`; unknown avg `11.5523` n `934`
- 4h: commodity avg `-0.129` n `12`; crypto_alt avg `0.9304` n `234`; crypto_major avg `0.2935` n `8`; equity avg `0.4346` n `140`; fx avg `-0.0146` n `6`; index avg `0.0868` n `26`; metal avg `0.3879` n `20`; unknown avg `6.4939` n `894`
- 24h: commodity avg `0.1451` n `12`; crypto_alt avg `2.0774` n `234`; crypto_major avg `0.6833` n `8`; equity avg `0.8452` n `140`; fx avg `-0.2895` n `6`; index avg `0.1304` n `26`; metal avg `0.3076` n `20`; unknown avg `1.4423` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
