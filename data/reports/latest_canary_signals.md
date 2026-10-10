# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T09:07:27.773816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.0091` n `235`; crypto_major avg `0.021` n `8`; equity avg `-0.0042` n `150`; fx avg `-0.0014` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.0352` n `1115`
- 1h: commodity avg `-0.0127` n `13`; crypto_alt avg `-0.0293` n `235`; crypto_major avg `-0.0238` n `8`; equity avg `-0.0088` n `150`; fx avg `-0.0281` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.3532` n `1115`
- 4h: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.1991` n `235`; crypto_major avg `0.1538` n `8`; equity avg `-0.0992` n `150`; fx avg `-0.0124` n `6`; index avg `-0.039` n `26`; metal avg `0.0059` n `20`; unknown avg `0.8556` n `1082`
- 24h: commodity avg `0.0802` n `13`; crypto_alt avg `1.3697` n `235`; crypto_major avg `0.1061` n `8`; equity avg `-0.267` n `150`; fx avg `-0.0293` n `6`; index avg `-0.0516` n `26`; metal avg `0.0508` n `20`; unknown avg `632.6831` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
