# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T03:52:29.860698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0567` n `13`; crypto_alt avg `-0.4258` n `237`; crypto_major avg `-0.429` n `8`; equity avg `-0.1542` n `152`; fx avg `0.0131` n `6`; index avg `-0.0113` n `26`; metal avg `-0.0285` n `20`; unknown avg `-0.1506` n `1240`
- 1h: commodity avg `-0.03` n `13`; crypto_alt avg `-0.1948` n `237`; crypto_major avg `-0.1339` n `8`; equity avg `0.1664` n `152`; fx avg `0.0087` n `6`; index avg `0.0559` n `26`; metal avg `0.1024` n `20`; unknown avg `0.2032` n `1240`
- 4h: commodity avg `-0.2453` n `13`; crypto_alt avg `-1.1243` n `237`; crypto_major avg `-0.9053` n `8`; equity avg `-0.8321` n `152`; fx avg `-0.014` n `6`; index avg `-0.0132` n `26`; metal avg `0.0407` n `20`; unknown avg `2.3249` n `1162`
- 24h: commodity avg `-0.6261` n `13`; crypto_alt avg `-2.1516` n `237`; crypto_major avg `-1.9226` n `8`; equity avg `-0.8854` n `152`; fx avg `0.0523` n `6`; index avg `-0.0147` n `26`; metal avg `0.1828` n `20`; unknown avg `-0.1185` n `989`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2458`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
