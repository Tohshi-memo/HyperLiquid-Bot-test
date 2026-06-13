# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T12:22:30.981952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0455` n `12`; crypto_alt avg `0.1608` n `228`; crypto_major avg `0.1475` n `8`; equity avg `0.0099` n `74`; fx avg `-0.0021` n `6`; index avg `-0.0157` n `23`; metal avg `-0.1205` n `18`; unknown avg `-0.0737` n `644`
- 1h: commodity avg `-0.1028` n `12`; crypto_alt avg `0.148` n `228`; crypto_major avg `0.1358` n `8`; equity avg `0.0035` n `74`; fx avg `-0.0005` n `6`; index avg `-0.0076` n `23`; metal avg `0.1311` n `18`; unknown avg `0.0186` n `644`
- 4h: commodity avg `-0.2407` n `12`; crypto_alt avg `0.7043` n `228`; crypto_major avg `0.4347` n `8`; equity avg `-0.0156` n `74`; fx avg `-0.009` n `6`; index avg `0.0938` n `23`; metal avg `0.0353` n `18`; unknown avg `0.2907` n `635`
- 24h: commodity avg `-0.4817` n `12`; crypto_alt avg `1.0623` n `228`; crypto_major avg `0.2406` n `8`; equity avg `-0.5487` n `74`; fx avg `0.0256` n `6`; index avg `0.6909` n `23`; metal avg `0.6504` n `18`; unknown avg `28.0342` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
