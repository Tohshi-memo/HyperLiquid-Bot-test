# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T15:37:32.405431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0611` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0448` n `12`; crypto_alt avg `-0.3246` n `234`; crypto_major avg `-0.4553` n `8`; equity avg `-0.1023` n `141`; fx avg `0.0078` n `6`; index avg `-0.0155` n `26`; metal avg `0.0233` n `20`; unknown avg `4.5142` n `960`
- 1h: commodity avg `0.1163` n `12`; crypto_alt avg `-0.2909` n `234`; crypto_major avg `-0.4539` n `8`; equity avg `0.1765` n `141`; fx avg `-0.0185` n `6`; index avg `0.0428` n `26`; metal avg `0.1384` n `20`; unknown avg `12.4731` n `958`
- 4h: commodity avg `0.2089` n `12`; crypto_alt avg `-1.0533` n `234`; crypto_major avg `-1.1668` n `8`; equity avg `-1.0019` n `141`; fx avg `-0.0261` n `6`; index avg `-0.1057` n `26`; metal avg `-0.0801` n `20`; unknown avg `37.7764` n `916`
- 24h: commodity avg `-0.7286` n `12`; crypto_alt avg `1.4405` n `234`; crypto_major avg `0.4899` n `8`; equity avg `0.7419` n `141`; fx avg `-0.2498` n `6`; index avg `0.2328` n `26`; metal avg `0.2728` n `20`; unknown avg `17.2629` n `795`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
