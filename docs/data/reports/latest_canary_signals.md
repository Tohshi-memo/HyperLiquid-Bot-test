# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T02:22:27.577332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `13`; crypto_alt avg `-0.3109` n `237`; crypto_major avg `-0.1833` n `8`; equity avg `-0.0219` n `152`; fx avg `0.0` n `6`; index avg `0.0002` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.823` n `1231`
- 1h: commodity avg `-0.0035` n `13`; crypto_alt avg `-0.2874` n `237`; crypto_major avg `0.1354` n `8`; equity avg `-0.0192` n `152`; fx avg `-0.002` n `6`; index avg `0.0075` n `26`; metal avg `0.0052` n `20`; unknown avg `109.0442` n `1225`
- 4h: commodity avg `-0.0659` n `13`; crypto_alt avg `0.0973` n `237`; crypto_major avg `0.7706` n `8`; equity avg `0.1958` n `152`; fx avg `-0.0046` n `6`; index avg `0.0194` n `26`; metal avg `0.0293` n `20`; unknown avg `158.5082` n `1215`
- 24h: commodity avg `-0.0191` n `13`; crypto_alt avg `-1.2835` n `237`; crypto_major avg `-0.1502` n `8`; equity avg `-0.055` n `152`; fx avg `-0.0358` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0783` n `20`; unknown avg `0.5339` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
