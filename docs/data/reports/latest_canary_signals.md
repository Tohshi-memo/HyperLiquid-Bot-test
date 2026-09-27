# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T13:07:33.317683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.6882` n `234`; crypto_major avg `-0.6096` n `8`; equity avg `-0.0614` n `141`; fx avg `0.0051` n `6`; index avg `-0.0112` n `26`; metal avg `-0.0073` n `20`; unknown avg `0.3667` n `960`
- 1h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.8178` n `234`; crypto_major avg `-0.5491` n `8`; equity avg `-0.0484` n `141`; fx avg `0.0118` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0138` n `20`; unknown avg `0.6042` n `960`
- 4h: commodity avg `0.027` n `12`; crypto_alt avg `-0.4441` n `234`; crypto_major avg `-0.1184` n `8`; equity avg `-0.0235` n `141`; fx avg `0.0036` n `6`; index avg `-0.02` n `26`; metal avg `-0.012` n `20`; unknown avg `2.1861` n `953`
- 24h: commodity avg `0.0431` n `12`; crypto_alt avg `0.0082` n `234`; crypto_major avg `0.2955` n `8`; equity avg `0.2983` n `141`; fx avg `-0.0333` n `6`; index avg `0.0306` n `26`; metal avg `-0.0213` n `20`; unknown avg `64.1423` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
