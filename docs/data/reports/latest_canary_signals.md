# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T07:42:33.880272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0327` n `12`; crypto_alt avg `-0.2392` n `234`; crypto_major avg `-0.2727` n `8`; equity avg `-0.0637` n `141`; fx avg `0.0144` n `6`; index avg `-0.0148` n `26`; metal avg `0.0059` n `20`; unknown avg `2.2242` n `946`
- 1h: commodity avg `0.1056` n `12`; crypto_alt avg `0.1205` n `234`; crypto_major avg `0.0029` n `8`; equity avg `-0.0771` n `141`; fx avg `0.0105` n `6`; index avg `-0.011` n `26`; metal avg `-0.0468` n `20`; unknown avg `2.7176` n `944`
- 4h: commodity avg `0.0451` n `12`; crypto_alt avg `0.4295` n `234`; crypto_major avg `-0.1665` n `8`; equity avg `0.2596` n `141`; fx avg `-0.0169` n `6`; index avg `0.0672` n `26`; metal avg `-0.0209` n `20`; unknown avg `1.179` n `906`
- 24h: commodity avg `0.4243` n `12`; crypto_alt avg `1.4645` n `234`; crypto_major avg `-0.434` n `8`; equity avg `0.8054` n `141`; fx avg `-0.1554` n `6`; index avg `0.1264` n `26`; metal avg `-0.2675` n `20`; unknown avg `12.205` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
