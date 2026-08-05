# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T09:37:32.733676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.042` n `12`; crypto_alt avg `-0.0314` n `230`; crypto_major avg `-0.0375` n `8`; equity avg `0.2084` n `108`; fx avg `0.0075` n `6`; index avg `0.0272` n `25`; metal avg `0.0336` n `20`; unknown avg `0.0002` n `781`
- 1h: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.1` n `230`; crypto_major avg `-0.0381` n `8`; equity avg `0.2377` n `108`; fx avg `-0.02` n `6`; index avg `0.0314` n `25`; metal avg `-0.0416` n `20`; unknown avg `0.6161` n `781`
- 4h: commodity avg `0.3139` n `12`; crypto_alt avg `-0.0771` n `230`; crypto_major avg `0.0594` n `8`; equity avg `-0.7194` n `108`; fx avg `0.0353` n `6`; index avg `-0.0843` n `25`; metal avg `0.0201` n `20`; unknown avg `0.7048` n `749`
- 24h: commodity avg `-1.2827` n `12`; crypto_alt avg `0.8059` n `230`; crypto_major avg `1.1746` n `8`; equity avg `2.9161` n `108`; fx avg `-0.0388` n `6`; index avg `0.6772` n `25`; metal avg `1.1721` n `20`; unknown avg `0.1825` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
