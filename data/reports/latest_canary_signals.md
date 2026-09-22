# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T12:37:37.156281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0724` n `12`; crypto_alt avg `0.2648` n `234`; crypto_major avg `0.1567` n `8`; equity avg `-0.0106` n `140`; fx avg `0.0018` n `6`; index avg `0.0145` n `26`; metal avg `0.017` n `20`; unknown avg `-0.2484` n `944`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `0.3842` n `234`; crypto_major avg `0.2374` n `8`; equity avg `-0.0655` n `140`; fx avg `0.0373` n `6`; index avg `0.0037` n `26`; metal avg `0.2288` n `20`; unknown avg `3.238` n `936`
- 4h: commodity avg `-0.4148` n `12`; crypto_alt avg `-0.2444` n `234`; crypto_major avg `0.3509` n `8`; equity avg `0.6345` n `140`; fx avg `-0.0049` n `6`; index avg `0.1201` n `26`; metal avg `0.3246` n `20`; unknown avg `2.7749` n `934`
- 24h: commodity avg `-0.4865` n `12`; crypto_alt avg `0.0894` n `234`; crypto_major avg `1.2859` n `8`; equity avg `0.7986` n `140`; fx avg `-0.2602` n `6`; index avg `0.2444` n `26`; metal avg `-0.1287` n `20`; unknown avg `1108.2913` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
