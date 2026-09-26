# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T23:52:32.838084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.1341` n `234`; crypto_major avg `0.0113` n `8`; equity avg `0.0097` n `141`; fx avg `-0.0018` n `6`; index avg `0.0013` n `26`; metal avg `0.0066` n `20`; unknown avg `0.701` n `961`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `0.3238` n `234`; crypto_major avg `0.2146` n `8`; equity avg `0.0149` n `141`; fx avg `-0.0055` n `6`; index avg `0.0016` n `26`; metal avg `0.0095` n `20`; unknown avg `3.4355` n `959`
- 4h: commodity avg `0.0101` n `12`; crypto_alt avg `0.1242` n `234`; crypto_major avg `0.3194` n `8`; equity avg `0.0556` n `141`; fx avg `-0.0276` n `6`; index avg `-0.0029` n `26`; metal avg `0.0107` n `20`; unknown avg `167.8787` n `929`
- 24h: commodity avg `0.302` n `12`; crypto_alt avg `0.5915` n `234`; crypto_major avg `-0.663` n `8`; equity avg `0.0439` n `141`; fx avg `0.0154` n `6`; index avg `-0.0575` n `26`; metal avg `-0.0114` n `20`; unknown avg `4.3112` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
