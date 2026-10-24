# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T22:37:29.706889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `13`; crypto_alt avg `0.2513` n `237`; crypto_major avg `0.2294` n `8`; equity avg `0.0734` n `152`; fx avg `-0.0015` n `6`; index avg `0.0057` n `26`; metal avg `0.0066` n `20`; unknown avg `0.1201` n `1231`
- 1h: commodity avg `0.0045` n `13`; crypto_alt avg `0.3925` n `237`; crypto_major avg `0.2448` n `8`; equity avg `0.1007` n `152`; fx avg `-0.0025` n `6`; index avg `0.0077` n `26`; metal avg `0.0111` n `20`; unknown avg `0.0287` n `1185`
- 4h: commodity avg `0.0106` n `13`; crypto_alt avg `0.7882` n `237`; crypto_major avg `0.7107` n `8`; equity avg `0.3133` n `152`; fx avg `-0.0116` n `6`; index avg `0.0447` n `26`; metal avg `0.0243` n `20`; unknown avg `1.8335` n `1137`
- 24h: commodity avg `0.0058` n `13`; crypto_alt avg `-0.9583` n `237`; crypto_major avg `-0.7614` n `8`; equity avg `-0.0379` n `152`; fx avg `-0.0833` n `6`; index avg `-0.0107` n `26`; metal avg `-0.1128` n `20`; unknown avg `0.1545` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
