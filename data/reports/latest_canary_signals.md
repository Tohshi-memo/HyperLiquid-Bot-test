# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T02:07:26.602105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.1688` n `233`; crypto_major avg `-0.1065` n `8`; equity avg `0.1268` n `136`; fx avg `0.0222` n `6`; index avg `0.0137` n `27`; metal avg `0.0876` n `20`; unknown avg `0.3348` n `906`
- 1h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.1351` n `233`; crypto_major avg `0.0902` n `8`; equity avg `-0.0183` n `136`; fx avg `0.0452` n `6`; index avg `-0.0049` n `27`; metal avg `0.0795` n `20`; unknown avg `0.1768` n `906`
- 4h: commodity avg `0.1103` n `12`; crypto_alt avg `-0.6245` n `233`; crypto_major avg `-0.8021` n `8`; equity avg `0.2622` n `136`; fx avg `0.0715` n `6`; index avg `0.0946` n `27`; metal avg `0.0262` n `20`; unknown avg `0.7647` n `892`
- 24h: commodity avg `0.0383` n `12`; crypto_alt avg `0.1173` n `233`; crypto_major avg `1.4946` n `8`; equity avg `-0.0474` n `136`; fx avg `0.0866` n `6`; index avg `-0.0405` n `27`; metal avg `-0.3926` n `20`; unknown avg `5.1761` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
