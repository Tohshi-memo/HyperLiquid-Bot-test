# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T04:07:28.579110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.2826` n `234`; crypto_major avg `-0.0373` n `8`; equity avg `0.0232` n `140`; fx avg `-0.0128` n `6`; index avg `0.0038` n `26`; metal avg `0.0063` n `20`; unknown avg `1.9977` n `937`
- 1h: commodity avg `-0.1104` n `12`; crypto_alt avg `0.4934` n `234`; crypto_major avg `0.5743` n `8`; equity avg `0.0988` n `140`; fx avg `0.0013` n `6`; index avg `0.0183` n `26`; metal avg `0.0564` n `20`; unknown avg `0.9904` n `937`
- 4h: commodity avg `-0.1455` n `12`; crypto_alt avg `0.711` n `234`; crypto_major avg `1.1077` n `8`; equity avg `-0.2013` n `140`; fx avg `-0.029` n `6`; index avg `-0.0706` n `26`; metal avg `-0.2437` n `20`; unknown avg `1.4858` n `937`
- 24h: commodity avg `-0.1523` n `12`; crypto_alt avg `3.4942` n `234`; crypto_major avg `1.7081` n `8`; equity avg `0.5894` n `140`; fx avg `-0.2016` n `6`; index avg `0.0434` n `26`; metal avg `0.1702` n `20`; unknown avg `1.7333` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
