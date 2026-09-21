# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T04:22:36.321291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0007` n `234`; crypto_major avg `0.0329` n `8`; equity avg `0.0644` n `140`; fx avg `-0.0041` n `6`; index avg `0.0178` n `26`; metal avg `0.0745` n `20`; unknown avg `0.9703` n `944`
- 1h: commodity avg `0.0369` n `12`; crypto_alt avg `0.2344` n `234`; crypto_major avg `-0.2413` n `8`; equity avg `-0.0062` n `140`; fx avg `0.0256` n `6`; index avg `0.0104` n `26`; metal avg `0.0386` n `20`; unknown avg `56.07` n `936`
- 4h: commodity avg `-0.2641` n `12`; crypto_alt avg `-0.0237` n `234`; crypto_major avg `-0.7547` n `8`; equity avg `0.201` n `140`; fx avg `-0.0415` n `6`; index avg `0.0695` n `26`; metal avg `0.0961` n `20`; unknown avg `54.0632` n `935`
- 24h: commodity avg `-0.657` n `12`; crypto_alt avg `3.5321` n `234`; crypto_major avg `2.5071` n `8`; equity avg `1.1292` n `140`; fx avg `-0.0152` n `6`; index avg `0.2236` n `26`; metal avg `0.0771` n `20`; unknown avg `4.7815` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
