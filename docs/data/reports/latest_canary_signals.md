# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T17:37:26.459171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0131` n `234`; crypto_major avg `-0.0095` n `8`; equity avg `0.0384` n `141`; fx avg `0.0015` n `6`; index avg `0.0161` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.7904` n `962`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.3082` n `234`; crypto_major avg `0.1255` n `8`; equity avg `0.0681` n `141`; fx avg `-0.0055` n `6`; index avg `0.0016` n `26`; metal avg `0.0008` n `20`; unknown avg `2.712` n `960`
- 4h: commodity avg `-0.1388` n `12`; crypto_alt avg `0.0514` n `234`; crypto_major avg `-0.5788` n `8`; equity avg `0.0344` n `141`; fx avg `0.0071` n `6`; index avg `0.0062` n `26`; metal avg `0.0023` n `20`; unknown avg `7.5149` n `954`
- 24h: commodity avg `-0.1202` n `12`; crypto_alt avg `-0.4525` n `234`; crypto_major avg `-0.1225` n `8`; equity avg `0.2858` n `141`; fx avg `-0.0174` n `6`; index avg `0.0145` n `26`; metal avg `-0.0099` n `20`; unknown avg `4.1751` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
