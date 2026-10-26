# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T04:52:25.426798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `0.1856` n `237`; crypto_major avg `0.1291` n `8`; equity avg `0.0546` n `152`; fx avg `0.0058` n `6`; index avg `0.0066` n `26`; metal avg `0.0066` n `20`; unknown avg `0.0752` n `1240`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `0.9454` n `237`; crypto_major avg `0.9169` n `8`; equity avg `0.3679` n `152`; fx avg `0.0045` n `6`; index avg `0.0512` n `26`; metal avg `0.0253` n `20`; unknown avg `2.0114` n `1230`
- 4h: commodity avg `-0.163` n `13`; crypto_alt avg `-0.153` n `237`; crypto_major avg `-0.0749` n `8`; equity avg `-0.0311` n `152`; fx avg `-0.0315` n `6`; index avg `0.0693` n `26`; metal avg `0.1148` n `20`; unknown avg `0.2145` n `1168`
- 24h: commodity avg `-0.6028` n `13`; crypto_alt avg `-1.2727` n `237`; crypto_major avg `-1.2129` n `8`; equity avg `-0.5876` n `152`; fx avg `0.0501` n `6`; index avg `0.0278` n `26`; metal avg `0.1737` n `20`; unknown avg `-0.3274` n `985`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2519`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
