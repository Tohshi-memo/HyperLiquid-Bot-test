# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T19:37:29.753789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.449` n `233`; crypto_major avg `-0.3405` n `8`; equity avg `-0.115` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0666` n `20`; unknown avg `4.0932` n `797`
- 1h: commodity avg `0.0207` n `12`; crypto_alt avg `-0.8834` n `233`; crypto_major avg `-0.5837` n `8`; equity avg `-0.1497` n `134`; fx avg `-0.0029` n `6`; index avg `0.0134` n `26`; metal avg `-0.1396` n `20`; unknown avg `15.9982` n `795`
- 4h: commodity avg `-0.1658` n `12`; crypto_alt avg `-0.1292` n `233`; crypto_major avg `-0.2651` n `8`; equity avg `-0.0408` n `134`; fx avg `0.0053` n `6`; index avg `0.0144` n `26`; metal avg `-0.0616` n `20`; unknown avg `1.3017` n `789`
- 24h: commodity avg `0.1856` n `12`; crypto_alt avg `-1.0957` n `233`; crypto_major avg `-0.5074` n `8`; equity avg `-0.3203` n `134`; fx avg `-0.0327` n `6`; index avg `-0.1586` n `26`; metal avg `0.4485` n `20`; unknown avg `5.7954` n `699`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
