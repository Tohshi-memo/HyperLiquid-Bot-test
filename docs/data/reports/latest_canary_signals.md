# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T00:37:23.453593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0661` n `12`; crypto_alt avg `-0.0679` n `234`; crypto_major avg `-0.0822` n `8`; equity avg `0.1968` n `140`; fx avg `-0.0191` n `6`; index avg `0.0204` n `26`; metal avg `0.0774` n `20`; unknown avg `1.1947` n `943`
- 1h: commodity avg `-0.1525` n `12`; crypto_alt avg `0.8806` n `234`; crypto_major avg `0.9165` n `8`; equity avg `0.3391` n `140`; fx avg `-0.0306` n `6`; index avg `0.0323` n `26`; metal avg `0.0017` n `20`; unknown avg `16.6451` n `935`
- 4h: commodity avg `-0.4871` n `12`; crypto_alt avg `1.035` n `234`; crypto_major avg `1.4142` n `8`; equity avg `0.81` n `140`; fx avg `0.0049` n `6`; index avg `0.1216` n `26`; metal avg `0.0646` n `20`; unknown avg `4.1442` n `883`
- 24h: commodity avg `-0.2357` n `12`; crypto_alt avg `1.5167` n `234`; crypto_major avg `1.4251` n `8`; equity avg `0.7104` n `140`; fx avg `0.0125` n `6`; index avg `0.1129` n `26`; metal avg `0.0188` n `20`; unknown avg `3.6172` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
