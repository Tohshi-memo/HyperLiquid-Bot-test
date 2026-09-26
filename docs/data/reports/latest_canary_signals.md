# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T03:52:26.729927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.2194` n `234`; crypto_major avg `-0.1593` n `8`; equity avg `-0.0125` n `141`; fx avg `-0.0032` n `6`; index avg `-0.0001` n `26`; metal avg `0.0026` n `20`; unknown avg `0.7166` n `961`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.1933` n `234`; crypto_major avg `-0.323` n `8`; equity avg `-0.0467` n `141`; fx avg `0.0202` n `6`; index avg `0.0037` n `26`; metal avg `0.0007` n `20`; unknown avg `0.2674` n `959`
- 4h: commodity avg `0.2954` n `12`; crypto_alt avg `-0.6932` n `234`; crypto_major avg `-0.5402` n `8`; equity avg `-0.1545` n `141`; fx avg `0.0053` n `6`; index avg `-0.0411` n `26`; metal avg `-0.0123` n `20`; unknown avg `-0.1536` n `952`
- 24h: commodity avg `0.0752` n `12`; crypto_alt avg `3.2732` n `234`; crypto_major avg `1.1362` n `8`; equity avg `-0.3332` n `141`; fx avg `-0.102` n `6`; index avg `0.1375` n `26`; metal avg `0.2314` n `20`; unknown avg `1126.1735` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
