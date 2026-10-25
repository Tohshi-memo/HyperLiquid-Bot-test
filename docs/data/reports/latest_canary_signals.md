# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T05:07:29.796613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `-0.1251` n `237`; crypto_major avg `-0.1157` n `8`; equity avg `-0.045` n `152`; fx avg `0.0006` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0064` n `20`; unknown avg `-0.0646` n `1229`
- 1h: commodity avg `-0.0178` n `13`; crypto_alt avg `-0.0925` n `237`; crypto_major avg `0.0601` n `8`; equity avg `0.0054` n `152`; fx avg `0.0054` n `6`; index avg `-0.0036` n `26`; metal avg `0.0261` n `20`; unknown avg `4.7577` n `1229`
- 4h: commodity avg `-0.0342` n `13`; crypto_alt avg `-0.3254` n `237`; crypto_major avg `0.289` n `8`; equity avg `0.0506` n `152`; fx avg `0.004` n `6`; index avg `0.0174` n `26`; metal avg `0.0252` n `20`; unknown avg `0.1542` n `1205`
- 24h: commodity avg `0.0207` n `13`; crypto_alt avg `-1.2455` n `237`; crypto_major avg `0.0505` n `8`; equity avg `0.0051` n `152`; fx avg `-0.0246` n `6`; index avg `0.0034` n `26`; metal avg `-0.0618` n `20`; unknown avg `6.2171` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
