# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T21:37:29.419541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `13`; crypto_alt avg `0.0075` n `235`; crypto_major avg `0.023` n `8`; equity avg `0.0085` n `150`; fx avg `-0.0031` n `6`; index avg `-0.0093` n `26`; metal avg `0.003` n `20`; unknown avg `1.574` n `1117`
- 1h: commodity avg `0.0234` n `13`; crypto_alt avg `0.203` n `235`; crypto_major avg `0.0653` n `8`; equity avg `0.0428` n `150`; fx avg `-0.0062` n `6`; index avg `-0.0058` n `26`; metal avg `0.0031` n `20`; unknown avg `3.6105` n `1109`
- 4h: commodity avg `0.0583` n `13`; crypto_alt avg `0.4986` n `235`; crypto_major avg `0.0429` n `8`; equity avg `0.0764` n `150`; fx avg `-0.0045` n `6`; index avg `-0.0006` n `26`; metal avg `0.0057` n `20`; unknown avg `2.9735` n `1001`
- 24h: commodity avg `-0.1097` n `13`; crypto_alt avg `2.8787` n `235`; crypto_major avg `0.9747` n `8`; equity avg `0.2138` n `150`; fx avg `-0.013` n `6`; index avg `0.0083` n `26`; metal avg `-0.0064` n `20`; unknown avg `2.2896` n `966`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
