# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T19:31:07.431918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.102` n `231`; crypto_major avg `-0.1357` n `8`; equity avg `0.0244` n `122`; fx avg `-0.0074` n `6`; index avg `0.002` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.2049` n `793`
- 1h: commodity avg `-0.0237` n `12`; crypto_alt avg `-0.1608` n `231`; crypto_major avg `-0.3405` n `8`; equity avg `0.1284` n `122`; fx avg `-0.0111` n `6`; index avg `0.0152` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.3941` n `793`
- 4h: commodity avg `-0.0708` n `12`; crypto_alt avg `0.203` n `231`; crypto_major avg `-0.0495` n `8`; equity avg `0.2927` n `122`; fx avg `-0.0151` n `6`; index avg `0.0582` n `25`; metal avg `0.0239` n `20`; unknown avg `0.7534` n `793`
- 24h: commodity avg `-0.0504` n `12`; crypto_alt avg `2.1476` n `231`; crypto_major avg `0.2477` n `8`; equity avg `0.8536` n `122`; fx avg `0.002` n `6`; index avg `0.1309` n `25`; metal avg `0.0768` n `20`; unknown avg `5.5244` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
