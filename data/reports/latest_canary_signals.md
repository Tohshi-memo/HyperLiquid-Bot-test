# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T12:07:31.507750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0403` n `12`; crypto_alt avg `0.3408` n `232`; crypto_major avg `0.2838` n `8`; equity avg `0.0185` n `134`; fx avg `0.0086` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0243` n `20`; unknown avg `-0.1094` n `786`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `0.3589` n `232`; crypto_major avg `0.2788` n `8`; equity avg `-0.0052` n `134`; fx avg `0.0099` n `6`; index avg `0.0007` n `26`; metal avg `-0.0455` n `20`; unknown avg `-0.4094` n `786`
- 4h: commodity avg `0.2536` n `12`; crypto_alt avg `1.0839` n `232`; crypto_major avg `0.4511` n `8`; equity avg `-0.0125` n `134`; fx avg `-0.0125` n `6`; index avg `-0.0569` n `26`; metal avg `-0.1501` n `20`; unknown avg `0.6627` n `776`
- 24h: commodity avg `0.1966` n `12`; crypto_alt avg `0.256` n `232`; crypto_major avg `-0.6022` n `8`; equity avg `0.2089` n `134`; fx avg `-0.0697` n `6`; index avg `-0.0139` n `26`; metal avg `-0.1902` n `20`; unknown avg `229.1032` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
