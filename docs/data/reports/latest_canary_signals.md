# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T05:37:26.412592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `13`; crypto_alt avg `-0.2996` n `237`; crypto_major avg `-0.2643` n `8`; equity avg `-0.0586` n `152`; fx avg `-0.0002` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.1233` n `1229`
- 1h: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.4148` n `237`; crypto_major avg `-0.3502` n `8`; equity avg `-0.0638` n `152`; fx avg `0.0015` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.4879` n `1229`
- 4h: commodity avg `-0.0363` n `13`; crypto_alt avg `-0.4751` n `237`; crypto_major avg `-0.0233` n `8`; equity avg `0.0259` n `152`; fx avg `0.0056` n `6`; index avg `0.0162` n `26`; metal avg `0.0249` n `20`; unknown avg `4.6546` n `1207`
- 24h: commodity avg `0.2721` n `13`; crypto_alt avg `-1.3851` n `237`; crypto_major avg `-0.072` n `8`; equity avg `0.0356` n `152`; fx avg `-0.0236` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0549` n `20`; unknown avg `5.8193` n `1058`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
