# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T23:37:30.220061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.0512` n `234`; crypto_major avg `-0.0057` n `8`; equity avg `0.0244` n `141`; fx avg `0.0024` n `6`; index avg `-0.0` n `26`; metal avg `-0.0208` n `20`; unknown avg `2.0414` n `962`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `0.5259` n `234`; crypto_major avg `0.4449` n `8`; equity avg `0.0155` n `141`; fx avg `-0.0058` n `6`; index avg `0.023` n `26`; metal avg `-0.0095` n `20`; unknown avg `5.6327` n `956`
- 4h: commodity avg `-0.2166` n `12`; crypto_alt avg `-0.3314` n `234`; crypto_major avg `-0.509` n `8`; equity avg `-0.3666` n `141`; fx avg `-0.0168` n `6`; index avg `-0.0769` n `26`; metal avg `-0.1903` n `20`; unknown avg `2.1303` n `886`
- 24h: commodity avg `-0.4206` n `12`; crypto_alt avg `0.5344` n `234`; crypto_major avg `-0.1884` n `8`; equity avg `-0.0223` n `141`; fx avg `-0.0201` n `6`; index avg `-0.0345` n `26`; metal avg `-0.1985` n `20`; unknown avg `5.1235` n `827`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
