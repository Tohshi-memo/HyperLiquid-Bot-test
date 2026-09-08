# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T09:07:39.310558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0406` n `12`; crypto_alt avg `-0.0156` n `232`; crypto_major avg `-0.0459` n `8`; equity avg `0.101` n `134`; fx avg `-0.0003` n `6`; index avg `0.035` n `26`; metal avg `0.0126` n `20`; unknown avg `2.0196` n `795`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1949` n `232`; crypto_major avg `0.0229` n `8`; equity avg `0.059` n `134`; fx avg `0.0211` n `6`; index avg `0.01` n `26`; metal avg `-0.017` n `20`; unknown avg `0.8393` n `787`
- 4h: commodity avg `0.29` n `12`; crypto_alt avg `-0.1264` n `232`; crypto_major avg `-0.0569` n `8`; equity avg `-0.9061` n `134`; fx avg `0.0888` n `6`; index avg `-0.222` n `26`; metal avg `-0.2596` n `20`; unknown avg `1.3053` n `755`
- 24h: commodity avg `0.5384` n `12`; crypto_alt avg `0.4898` n `232`; crypto_major avg `-0.8886` n `8`; equity avg `-0.6231` n `134`; fx avg `-0.0415` n `6`; index avg `-0.1566` n `26`; metal avg `-0.0146` n `20`; unknown avg `7507.5629` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
