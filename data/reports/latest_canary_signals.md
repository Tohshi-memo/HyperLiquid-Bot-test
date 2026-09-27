# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T10:37:24.693292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.0786` n `234`; crypto_major avg `-0.1393` n `8`; equity avg `-0.0028` n `141`; fx avg `-0.0027` n `6`; index avg `-0.0033` n `26`; metal avg `-0.005` n `20`; unknown avg `1.3832` n `962`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `0.0071` n `234`; crypto_major avg `0.0705` n `8`; equity avg `0.0039` n `141`; fx avg `-0.0103` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.0454` n `959`
- 4h: commodity avg `-0.0201` n `12`; crypto_alt avg `0.6729` n `234`; crypto_major avg `0.6706` n `8`; equity avg `0.1561` n `141`; fx avg `-0.0233` n `6`; index avg `0.0265` n `26`; metal avg `0.0082` n `20`; unknown avg `1.7527` n `943`
- 24h: commodity avg `0.0301` n `12`; crypto_alt avg `0.9431` n `234`; crypto_major avg `0.7868` n `8`; equity avg `0.3921` n `141`; fx avg `-0.0188` n `6`; index avg `0.04` n `26`; metal avg `-0.0025` n `20`; unknown avg `5.4257` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
