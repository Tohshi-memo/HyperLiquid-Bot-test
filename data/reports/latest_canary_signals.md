# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T04:37:31.884429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.215` n `234`; crypto_major avg `-0.07` n `8`; equity avg `-0.0299` n `141`; fx avg `0.0143` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0108` n `20`; unknown avg `23.9348` n `962`
- 1h: commodity avg `0.0674` n `12`; crypto_alt avg `0.2219` n `234`; crypto_major avg `0.0953` n `8`; equity avg `0.2054` n `141`; fx avg `-0.0042` n `6`; index avg `0.0406` n `26`; metal avg `0.0311` n `20`; unknown avg `25.0523` n `952`
- 4h: commodity avg `0.145` n `12`; crypto_alt avg `-2.0159` n `234`; crypto_major avg `-1.0907` n `8`; equity avg `-1.0756` n `141`; fx avg `-0.0085` n `6`; index avg `-0.1128` n `26`; metal avg `-0.3537` n `20`; unknown avg `213.5686` n `936`
- 24h: commodity avg `-0.3573` n `12`; crypto_alt avg `-0.8258` n `234`; crypto_major avg `-1.1031` n `8`; equity avg `-1.3795` n `141`; fx avg `0.0602` n `6`; index avg `-0.1322` n `26`; metal avg `-0.6887` n `20`; unknown avg `9.5743` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
