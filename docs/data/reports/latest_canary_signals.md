# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T21:37:28.299364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `0.3153` n `234`; crypto_major avg `0.2245` n `8`; equity avg `0.047` n `141`; fx avg `0.0007` n `6`; index avg `0.0009` n `26`; metal avg `0.0074` n `20`; unknown avg `-0.0484` n `961`
- 1h: commodity avg `0.0391` n `12`; crypto_alt avg `0.2674` n `234`; crypto_major avg `0.2039` n `8`; equity avg `0.0073` n `141`; fx avg `-0.007` n `6`; index avg `-0.0063` n `26`; metal avg `0.0045` n `20`; unknown avg `0.0126` n `959`
- 4h: commodity avg `0.0625` n `12`; crypto_alt avg `-0.9512` n `234`; crypto_major avg `-0.2054` n `8`; equity avg `-0.0219` n `141`; fx avg `-0.0081` n `6`; index avg `-0.0264` n `26`; metal avg `0.0114` n `20`; unknown avg `-0.0703` n `953`
- 24h: commodity avg `0.3626` n `12`; crypto_alt avg `1.653` n `234`; crypto_major avg `-0.0943` n `8`; equity avg `-0.0033` n `141`; fx avg `0.0323` n `6`; index avg `-0.0615` n `26`; metal avg `-0.0244` n `20`; unknown avg `4.3637` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
