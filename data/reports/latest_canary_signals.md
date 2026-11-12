# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T04:07:27.079126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `13`; crypto_alt avg `0.0216` n `239`; crypto_major avg `0.0941` n `8`; equity avg `0.1523` n `161`; fx avg `-0.0074` n `6`; index avg `0.0353` n `27`; metal avg `-0.0141` n `20`; unknown avg `1.8328` n `1252`
- 1h: commodity avg `-0.067` n `13`; crypto_alt avg `0.0022` n `239`; crypto_major avg `-0.055` n `8`; equity avg `-0.4689` n `161`; fx avg `-0.018` n `6`; index avg `-0.0329` n `27`; metal avg `-0.0359` n `20`; unknown avg `0.1108` n `1246`
- 4h: commodity avg `-0.1171` n `13`; crypto_alt avg `-0.2926` n `239`; crypto_major avg `-0.1141` n `8`; equity avg `0.0378` n `161`; fx avg `-0.0704` n `6`; index avg `0.0186` n `27`; metal avg `0.1186` n `20`; unknown avg `21.8737` n `1246`
- 24h: commodity avg `0.0563` n `13`; crypto_alt avg `-1.9241` n `239`; crypto_major avg `-0.5023` n `8`; equity avg `0.4511` n `161`; fx avg `-0.2273` n `6`; index avg `0.0355` n `27`; metal avg `-0.4311` n `20`; unknown avg `1.6811` n `1137`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
