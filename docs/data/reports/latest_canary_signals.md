# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T19:52:37.641445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0326` n `12`; crypto_alt avg `0.0459` n `234`; crypto_major avg `0.0694` n `8`; equity avg `0.099` n `141`; fx avg `0.0015` n `6`; index avg `0.0183` n `26`; metal avg `0.0238` n `20`; unknown avg `9.2276` n `922`
- 1h: commodity avg `0.1789` n `12`; crypto_alt avg `0.2746` n `234`; crypto_major avg `-0.0393` n `8`; equity avg `-0.1179` n `141`; fx avg `-0.0006` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0239` n `20`; unknown avg `44.5485` n `913`
- 4h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.673` n `234`; crypto_major avg `0.581` n `8`; equity avg `0.7185` n `141`; fx avg `-0.0114` n `6`; index avg `0.1301` n `26`; metal avg `0.1687` n `20`; unknown avg `8.0269` n `901`
- 24h: commodity avg `1.0318` n `12`; crypto_alt avg `4.0278` n `234`; crypto_major avg `1.5033` n `8`; equity avg `-0.0773` n `141`; fx avg `0.0343` n `6`; index avg `-0.0457` n `26`; metal avg `-0.0232` n `20`; unknown avg `5.533` n `821`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
