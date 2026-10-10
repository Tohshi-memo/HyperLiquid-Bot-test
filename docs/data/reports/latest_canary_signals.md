# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T09:52:28.525011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0503` n `13`; crypto_alt avg `-0.0457` n `235`; crypto_major avg `-0.0834` n `8`; equity avg `0.0024` n `150`; fx avg `-0.0014` n `6`; index avg `0.0026` n `26`; metal avg `0.0035` n `20`; unknown avg `0.4049` n `1117`
- 1h: commodity avg `-0.222` n `13`; crypto_alt avg `-0.042` n `235`; crypto_major avg `-0.0416` n `8`; equity avg `0.0053` n `150`; fx avg `-0.0009` n `6`; index avg `0.01` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.0403` n `1115`
- 4h: commodity avg `-0.2303` n `13`; crypto_alt avg `-0.4433` n `235`; crypto_major avg `-0.1271` n `8`; equity avg `-0.0809` n `150`; fx avg `-0.0113` n `6`; index avg `-0.0252` n `26`; metal avg `0.0012` n `20`; unknown avg `0.3651` n `1082`
- 24h: commodity avg `-0.1173` n `13`; crypto_alt avg `1.4306` n `235`; crypto_major avg `0.0432` n `8`; equity avg `-0.202` n `150`; fx avg `-0.0321` n `6`; index avg `-0.0248` n `26`; metal avg `0.0536` n `20`; unknown avg `632.3714` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
