# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T20:52:27.096180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `13`; crypto_alt avg `0.263` n `237`; crypto_major avg `0.1853` n `8`; equity avg `0.0155` n `152`; fx avg `0.0085` n `6`; index avg `0.0082` n `26`; metal avg `-0.0117` n `20`; unknown avg `0.1201` n `1228`
- 1h: commodity avg `-0.0181` n `13`; crypto_alt avg `0.0847` n `237`; crypto_major avg `0.2758` n `8`; equity avg `0.2175` n `152`; fx avg `-0.0229` n `6`; index avg `0.044` n `26`; metal avg `-0.0339` n `20`; unknown avg `113.6568` n `1150`
- 4h: commodity avg `0.1399` n `13`; crypto_alt avg `-1.0638` n `237`; crypto_major avg `-0.5403` n `8`; equity avg `-0.3178` n `152`; fx avg `-0.0367` n `6`; index avg `-0.0` n `26`; metal avg `-0.1103` n `20`; unknown avg `0.1591` n `1149`
- 24h: commodity avg `0.3918` n `13`; crypto_alt avg `0.7681` n `237`; crypto_major avg `0.7901` n `8`; equity avg `1.5704` n `152`; fx avg `-0.0896` n `6`; index avg `0.1317` n `26`; metal avg `-0.1306` n `20`; unknown avg `0.1614` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
