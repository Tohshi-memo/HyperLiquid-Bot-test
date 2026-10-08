# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T06:20:10.928242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1286` n `13`; crypto_alt avg `-0.0744` n `235`; crypto_major avg `-0.1225` n `8`; equity avg `-0.1654` n `150`; fx avg `-0.0024` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0087` n `20`; unknown avg `0.0551` n `1071`
- 1h: commodity avg `0.1725` n `13`; crypto_alt avg `-0.4112` n `235`; crypto_major avg `-0.309` n `8`; equity avg `-0.4936` n `150`; fx avg `-0.0292` n `6`; index avg `-0.1037` n `26`; metal avg `-0.1379` n `20`; unknown avg `0.2118` n `1047`
- 4h: commodity avg `0.2539` n `13`; crypto_alt avg `-0.7668` n `235`; crypto_major avg `-0.8745` n `8`; equity avg `-0.8689` n `150`; fx avg `-0.0094` n `6`; index avg `-0.1395` n `26`; metal avg `-0.2257` n `20`; unknown avg `0.6052` n `1041`
- 24h: commodity avg `0.5212` n `13`; crypto_alt avg `-1.1305` n `235`; crypto_major avg `-2.3391` n `8`; equity avg `-1.6562` n `150`; fx avg `-0.151` n `6`; index avg `-0.2728` n `26`; metal avg `-0.2401` n `20`; unknown avg `416.7098` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
