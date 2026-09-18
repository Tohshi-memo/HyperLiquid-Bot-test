# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T10:07:32.700988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.135` n `234`; crypto_major avg `0.103` n `8`; equity avg `0.0279` n `140`; fx avg `-0.0183` n `6`; index avg `-0.014` n `26`; metal avg `0.0248` n `20`; unknown avg `0.1373` n `925`
- 1h: commodity avg `0.1545` n `12`; crypto_alt avg `0.298` n `234`; crypto_major avg `0.0848` n `8`; equity avg `-0.1515` n `140`; fx avg `0.0198` n `6`; index avg `-0.0505` n `26`; metal avg `-0.1049` n `20`; unknown avg `0.9399` n `925`
- 4h: commodity avg `-0.012` n `12`; crypto_alt avg `1.3219` n `234`; crypto_major avg `0.9188` n `8`; equity avg `0.058` n `140`; fx avg `0.1299` n `6`; index avg `-0.0132` n `26`; metal avg `0.0435` n `20`; unknown avg `1.557` n `901`
- 24h: commodity avg `-0.037` n `12`; crypto_alt avg `6.0371` n `234`; crypto_major avg `4.5929` n `8`; equity avg `1.6871` n `140`; fx avg `0.1941` n `6`; index avg `0.2056` n `26`; metal avg `0.6938` n `20`; unknown avg `2.9011` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
