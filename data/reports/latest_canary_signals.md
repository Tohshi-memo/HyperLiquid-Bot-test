# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T23:07:35.043185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0446` n `13`; crypto_alt avg `-0.0592` n `238`; crypto_major avg `-0.037` n `8`; equity avg `0.1786` n `155`; fx avg `-0.0037` n `6`; index avg `0.0501` n `27`; metal avg `0.033` n `20`; unknown avg `-0.0139` n `1192`
- 1h: commodity avg `-0.0674` n `13`; crypto_alt avg `-0.1684` n `238`; crypto_major avg `-0.0734` n `8`; equity avg `-0.0356` n `155`; fx avg `-0.0115` n `6`; index avg `0.0185` n `27`; metal avg `-0.0333` n `20`; unknown avg `7.1429` n `1168`
- 4h: commodity avg `-0.2206` n `13`; crypto_alt avg `0.3438` n `238`; crypto_major avg `0.1746` n `8`; equity avg `-0.7382` n `155`; fx avg `-0.0167` n `6`; index avg `-0.0626` n `27`; metal avg `0.0938` n `20`; unknown avg `4.3161` n `1064`
- 24h: commodity avg `0.1467` n `13`; crypto_alt avg `0.4498` n `238`; crypto_major avg `0.4033` n `8`; equity avg `0.9483` n `154`; fx avg `0.2389` n `6`; index avg `0.1679` n `27`; metal avg `-0.1557` n `20`; unknown avg `26.5021` n `1010`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
