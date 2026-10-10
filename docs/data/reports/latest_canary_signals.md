# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T14:52:24.463018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `0.0812` n `235`; crypto_major avg `-0.1273` n `8`; equity avg `0.0577` n `150`; fx avg `0.0` n `6`; index avg `0.015` n `26`; metal avg `0.0046` n `20`; unknown avg `0.6857` n `1117`
- 1h: commodity avg `0.0201` n `13`; crypto_alt avg `0.6511` n `235`; crypto_major avg `0.5396` n `8`; equity avg `0.1025` n `150`; fx avg `0.0013` n `6`; index avg `0.0243` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.314` n `1115`
- 4h: commodity avg `0.1053` n `13`; crypto_alt avg `0.9651` n `235`; crypto_major avg `0.6539` n `8`; equity avg `0.1495` n `150`; fx avg `-0.0102` n `6`; index avg `0.0145` n `26`; metal avg `0.0086` n `20`; unknown avg `0.6027` n `1109`
- 24h: commodity avg `-0.5197` n `13`; crypto_alt avg `2.6959` n `235`; crypto_major avg `0.8314` n `8`; equity avg `0.399` n `150`; fx avg `-0.0093` n `6`; index avg `0.0609` n `26`; metal avg `0.0327` n `20`; unknown avg `0.5338` n `936`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
