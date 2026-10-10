# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T09:22:27.814022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.0551` n `235`; crypto_major avg `0.0382` n `8`; equity avg `0.0086` n `150`; fx avg `0.003` n `6`; index avg `0.0075` n `26`; metal avg `-0.0099` n `20`; unknown avg `0.1062` n `1117`
- 1h: commodity avg `-0.0086` n `13`; crypto_alt avg `0.1204` n `235`; crypto_major avg `0.1018` n `8`; equity avg `0.0251` n `150`; fx avg `-0.0447` n `6`; index avg `0.005` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.5669` n `1115`
- 4h: commodity avg `-0.0334` n `13`; crypto_alt avg `-0.4063` n `235`; crypto_major avg `0.1171` n `8`; equity avg `-0.0854` n `150`; fx avg `-0.008` n `6`; index avg `-0.0317` n `26`; metal avg `-0.001` n `20`; unknown avg `0.7432` n `1082`
- 24h: commodity avg `0.0724` n `13`; crypto_alt avg `1.3057` n `235`; crypto_major avg `0.1586` n `8`; equity avg `-0.1881` n `150`; fx avg `-0.0328` n `6`; index avg `-0.0385` n `26`; metal avg `0.0316` n `20`; unknown avg `632.1308` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
