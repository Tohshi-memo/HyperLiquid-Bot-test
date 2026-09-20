# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T11:37:27.663120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.2076` n `234`; crypto_major avg `0.2108` n `8`; equity avg `0.0206` n `140`; fx avg `0.0104` n `6`; index avg `0.004` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.0182` n `943`
- 1h: commodity avg `-0.0121` n `12`; crypto_alt avg `0.271` n `234`; crypto_major avg `0.1417` n `8`; equity avg `0.0163` n `140`; fx avg `0.0157` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.1237` n `941`
- 4h: commodity avg `0.0037` n `12`; crypto_alt avg `-0.4119` n `234`; crypto_major avg `-0.0816` n `8`; equity avg `-0.0449` n `140`; fx avg `0.0113` n `6`; index avg `0.0045` n `26`; metal avg `-0.011` n `20`; unknown avg `0.2051` n `935`
- 24h: commodity avg `0.2363` n `12`; crypto_alt avg `-2.2618` n `234`; crypto_major avg `-2.1964` n `8`; equity avg `-0.2736` n `140`; fx avg `-0.0462` n `6`; index avg `-0.0436` n `26`; metal avg `-0.0283` n `20`; unknown avg `0.0585` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
