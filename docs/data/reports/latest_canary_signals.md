# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T09:52:26.737617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0785` n `13`; crypto_alt avg `0.0552` n `236`; crypto_major avg `0.0819` n `8`; equity avg `0.0102` n `151`; fx avg `-0.0178` n `6`; index avg `-0.0057` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.0341` n `1128`
- 1h: commodity avg `-0.1362` n `13`; crypto_alt avg `-0.0991` n `236`; crypto_major avg `0.0404` n `8`; equity avg `-0.0745` n `151`; fx avg `-0.0194` n `6`; index avg `-0.0186` n `26`; metal avg `0.1263` n `20`; unknown avg `-0.2974` n `1126`
- 4h: commodity avg `-0.0794` n `13`; crypto_alt avg `1.1055` n `236`; crypto_major avg `1.0632` n `8`; equity avg `-0.1778` n `151`; fx avg `-0.0451` n `6`; index avg `0.0522` n `26`; metal avg `0.2373` n `20`; unknown avg `4.4311` n `1092`
- 24h: commodity avg `-0.4725` n `13`; crypto_alt avg `-4.1134` n `236`; crypto_major avg `-2.8094` n `8`; equity avg `-5.8789` n `151`; fx avg `0.0765` n `6`; index avg `-0.9709` n `26`; metal avg `-0.3718` n `20`; unknown avg `2.1977` n `970`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1184`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0889`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0785`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0689`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0658`, n `666`, weak_sample_signal
