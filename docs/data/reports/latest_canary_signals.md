# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T01:22:34.437097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `0.2671` n `235`; crypto_major avg `0.1086` n `8`; equity avg `-0.0038` n `150`; fx avg `-0.0011` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0007` n `20`; unknown avg `-0.0543` n `1117`
- 1h: commodity avg `-0.0319` n `13`; crypto_alt avg `-0.0191` n `235`; crypto_major avg `-0.0539` n `8`; equity avg `-0.0179` n `150`; fx avg `-0.0031` n `6`; index avg `-0.006` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.1634` n `1115`
- 4h: commodity avg `0.1752` n `13`; crypto_alt avg `-0.3734` n `235`; crypto_major avg `-0.2054` n `8`; equity avg `-0.0472` n `150`; fx avg `0.0017` n `6`; index avg `-0.0085` n `26`; metal avg `0.0111` n `20`; unknown avg `3.449` n `1085`
- 24h: commodity avg `0.0597` n `13`; crypto_alt avg `1.4559` n `235`; crypto_major avg `0.4185` n `8`; equity avg `0.0811` n `150`; fx avg `-0.0124` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0144` n `20`; unknown avg `0.2795` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
