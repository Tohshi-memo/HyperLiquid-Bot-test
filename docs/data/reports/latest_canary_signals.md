# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T06:37:27.700604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0474` n `13`; crypto_alt avg `0.1663` n `235`; crypto_major avg `0.2643` n `8`; equity avg `-0.0029` n `151`; fx avg `0.0009` n `6`; index avg `-0.0175` n `26`; metal avg `0.0029` n `20`; unknown avg `0.3124` n `1133`
- 1h: commodity avg `0.1518` n `13`; crypto_alt avg `-0.0644` n `235`; crypto_major avg `0.1018` n `8`; equity avg `-0.2308` n `151`; fx avg `-0.0087` n `6`; index avg `-0.0475` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.2203` n `1103`
- 4h: commodity avg `0.2637` n `13`; crypto_alt avg `0.2424` n `235`; crypto_major avg `0.2872` n `8`; equity avg `-0.4348` n `151`; fx avg `0.0087` n `6`; index avg `-0.1079` n `26`; metal avg `-0.1566` n `20`; unknown avg `-0.0449` n `1043`
- 24h: commodity avg `-0.2391` n `13`; crypto_alt avg `2.6682` n `235`; crypto_major avg `1.7753` n `8`; equity avg `-0.536` n `151`; fx avg `-0.0577` n `6`; index avg `-0.0665` n `26`; metal avg `0.0506` n `20`; unknown avg `0.6223` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2048`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
