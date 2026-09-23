# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T21:37:31.619978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.486` n `234`; crypto_major avg `0.2916` n `8`; equity avg `0.0276` n `141`; fx avg `-0.0028` n `6`; index avg `0.002` n `26`; metal avg `-0.0074` n `20`; unknown avg `-0.0105` n `945`
- 1h: commodity avg `-0.0448` n `12`; crypto_alt avg `0.4164` n `234`; crypto_major avg `0.3178` n `8`; equity avg `0.0372` n `141`; fx avg `-0.016` n `6`; index avg `-0.002` n `26`; metal avg `0.0245` n `20`; unknown avg `-0.092` n `927`
- 4h: commodity avg `0.1842` n `12`; crypto_alt avg `-0.5048` n `234`; crypto_major avg `0.1809` n `8`; equity avg `-0.0822` n `141`; fx avg `-0.0424` n `6`; index avg `0.0229` n `26`; metal avg `0.117` n `20`; unknown avg `3.5453` n `845`
- 24h: commodity avg `0.5893` n `12`; crypto_alt avg `-3.6752` n `234`; crypto_major avg `-3.3597` n `8`; equity avg `-1.6084` n `140`; fx avg `0.0079` n `6`; index avg `-0.3569` n `26`; metal avg `-0.7975` n `20`; unknown avg `584.1218` n `820`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
