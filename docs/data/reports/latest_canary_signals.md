# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T10:37:26.306510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.1072` n `237`; crypto_major avg `-0.0944` n `8`; equity avg `0.002` n `152`; fx avg `0.0014` n `6`; index avg `-0.0074` n `26`; metal avg `-0.001` n `20`; unknown avg `0.5446` n `1227`
- 1h: commodity avg `0.0069` n `13`; crypto_alt avg `0.1182` n `237`; crypto_major avg `0.1212` n `8`; equity avg `0.1082` n `152`; fx avg `0.0119` n `6`; index avg `-0.0184` n `26`; metal avg `0.0207` n `20`; unknown avg `0.2728` n `1203`
- 4h: commodity avg `-0.0444` n `13`; crypto_alt avg `-0.8638` n `237`; crypto_major avg `-0.6481` n `8`; equity avg `-0.159` n `152`; fx avg `0.0023` n `6`; index avg `-0.0147` n `26`; metal avg `0.0158` n `20`; unknown avg `12.4503` n `1179`
- 24h: commodity avg `0.0349` n `13`; crypto_alt avg `-2.1208` n `237`; crypto_major avg `-0.4067` n `8`; equity avg `-0.0689` n `152`; fx avg `-0.0249` n `6`; index avg `0.0156` n `26`; metal avg `-0.0538` n `20`; unknown avg `11.4201` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
