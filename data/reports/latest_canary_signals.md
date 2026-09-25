# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T19:07:29.081176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1134` n `12`; crypto_alt avg `0.0022` n `234`; crypto_major avg `-0.0138` n `8`; equity avg `0.0697` n `141`; fx avg `-0.0074` n `6`; index avg `0.0085` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.0091` n `958`
- 1h: commodity avg `-0.0364` n `12`; crypto_alt avg `0.5282` n `234`; crypto_major avg `0.2597` n `8`; equity avg `0.0584` n `141`; fx avg `-0.0053` n `6`; index avg `0.0062` n `26`; metal avg `0.0607` n `20`; unknown avg `-0.0455` n `958`
- 4h: commodity avg `-0.2151` n `12`; crypto_alt avg `0.6811` n `234`; crypto_major avg `-0.0217` n `8`; equity avg `0.1907` n `141`; fx avg `-0.0294` n `6`; index avg `0.0818` n `26`; metal avg `0.1283` n `20`; unknown avg `0.2929` n `930`
- 24h: commodity avg `-0.8728` n `12`; crypto_alt avg `2.2124` n `234`; crypto_major avg `0.5661` n `8`; equity avg `0.1509` n `141`; fx avg `-0.2706` n `6`; index avg `0.2139` n `26`; metal avg `0.1794` n `20`; unknown avg `1597.279` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
