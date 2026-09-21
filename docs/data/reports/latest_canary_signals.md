# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T07:22:29.277338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.2369` n `234`; crypto_major avg `0.019` n `8`; equity avg `-0.0073` n `140`; fx avg `0.0227` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0313` n `20`; unknown avg `3.6484` n `944`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `-0.1676` n `234`; crypto_major avg `-0.1209` n `8`; equity avg `0.1497` n `140`; fx avg `-0.002` n `6`; index avg `0.0322` n `26`; metal avg `0.0223` n `20`; unknown avg `2.6199` n `920`
- 4h: commodity avg `0.0571` n `12`; crypto_alt avg `0.5191` n `234`; crypto_major avg `0.3215` n `8`; equity avg `0.157` n `140`; fx avg `0.0051` n `6`; index avg `0.0529` n `26`; metal avg `-0.0322` n `20`; unknown avg `2.4944` n `890`
- 24h: commodity avg `-0.5971` n `12`; crypto_alt avg `3.9965` n `234`; crypto_major avg `2.9383` n `8`; equity avg `1.3154` n `140`; fx avg `-0.0341` n `6`; index avg `0.2799` n `26`; metal avg `-0.0088` n `20`; unknown avg `2.6851` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
