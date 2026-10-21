# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T05:07:40.064502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0327` n `13`; crypto_alt avg `0.1721` n `237`; crypto_major avg `0.1896` n `8`; equity avg `-0.0095` n `151`; fx avg `0.0004` n `6`; index avg `-0.002` n `26`; metal avg `0.0337` n `20`; unknown avg `-0.1572` n `1198`
- 1h: commodity avg `-0.1123` n `13`; crypto_alt avg `-0.0117` n `237`; crypto_major avg `0.1276` n `8`; equity avg `0.0104` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0081` n `26`; metal avg `0.0079` n `20`; unknown avg `-0.2582` n `1198`
- 4h: commodity avg `-0.0531` n `13`; crypto_alt avg `0.3012` n `237`; crypto_major avg `-0.0043` n `8`; equity avg `-0.0834` n `151`; fx avg `-0.0481` n `6`; index avg `0.0321` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.9417` n `1191`
- 24h: commodity avg `-0.0536` n `13`; crypto_alt avg `2.4489` n `237`; crypto_major avg `1.5189` n `8`; equity avg `2.5074` n `151`; fx avg `-0.0103` n `6`; index avg `0.3504` n `26`; metal avg `-0.1507` n `20`; unknown avg `221.0664` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
