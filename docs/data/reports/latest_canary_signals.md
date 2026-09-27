# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T01:37:25.546742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `74.54` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `0.1614` n `234`; crypto_major avg `-0.0562` n `8`; equity avg `-0.034` n `141`; fx avg `-0.0062` n `6`; index avg `-0.0005` n `26`; metal avg `0.0027` n `20`; unknown avg `0.2184` n `961`
- 1h: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0228` n `234`; crypto_major avg `-0.0817` n `8`; equity avg `-0.0455` n `141`; fx avg `-0.0061` n `6`; index avg `-0.001` n `26`; metal avg `0.0025` n `20`; unknown avg `7.0462` n `957`
- 4h: commodity avg `-0.0899` n `12`; crypto_alt avg `-0.0172` n `234`; crypto_major avg `-0.0274` n `8`; equity avg `0.0255` n `141`; fx avg `-0.0086` n `6`; index avg `0.0068` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.051` n `927`
- 24h: commodity avg `-0.1528` n `12`; crypto_alt avg `0.4687` n `234`; crypto_major avg `-0.8505` n `8`; equity avg `0.2081` n `141`; fx avg `0.0096` n `6`; index avg `0.0042` n `26`; metal avg `0.0103` n `20`; unknown avg `4.2543` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
