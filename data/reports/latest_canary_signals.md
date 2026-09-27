# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T05:52:32.766379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.0768` n `234`; crypto_major avg `-0.0523` n `8`; equity avg `-0.0206` n `141`; fx avg `0.0` n `6`; index avg `0.0011` n `26`; metal avg `-0.0033` n `20`; unknown avg `7.1347` n `961`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `0.9126` n `234`; crypto_major avg `0.4878` n `8`; equity avg `0.0202` n `141`; fx avg `0.0094` n `6`; index avg `-0.0059` n `26`; metal avg `0.0006` n `20`; unknown avg `2.4671` n `959`
- 4h: commodity avg `0.0722` n `12`; crypto_alt avg `0.0639` n `234`; crypto_major avg `-0.0649` n `8`; equity avg `0.0486` n `141`; fx avg `0.0095` n `6`; index avg `0.0131` n `26`; metal avg `-0.0167` n `20`; unknown avg `-0.1761` n `949`
- 24h: commodity avg `0.0135` n `12`; crypto_alt avg `1.0605` n `234`; crypto_major avg `0.0495` n `8`; equity avg `0.2399` n `141`; fx avg `0.0277` n `6`; index avg `0.0038` n `26`; metal avg `-0.0162` n `20`; unknown avg `4.8236` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
