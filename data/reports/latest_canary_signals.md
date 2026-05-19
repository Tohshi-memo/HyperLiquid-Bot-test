# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T08:22:14.598285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.0685` n `228`; crypto_major avg `-0.0747` n `8`; equity avg `-0.1175` n `66`; fx avg `0.0073` n `6`; index avg `-0.1088` n `23`; metal avg `-0.0462` n `18`; unknown avg `-0.0813` n `383`
- 1h: commodity avg `-0.0934` n `12`; crypto_alt avg `-0.2422` n `228`; crypto_major avg `-0.1655` n `8`; equity avg `-0.1308` n `66`; fx avg `0.0115` n `6`; index avg `-0.0799` n `23`; metal avg `-0.0216` n `18`; unknown avg `-0.1739` n `383`
- 4h: commodity avg `0.2705` n `12`; crypto_alt avg `-0.0733` n `228`; crypto_major avg `0.1722` n `8`; equity avg `0.3094` n `66`; fx avg `0.0034` n `6`; index avg `0.1909` n `23`; metal avg `-0.0357` n `18`; unknown avg `-0.1299` n `363`
- 24h: commodity avg `0.5891` n `12`; crypto_alt avg `1.6414` n `228`; crypto_major avg `0.9509` n `8`; equity avg `-1.2152` n `66`; fx avg `0.3226` n `6`; index avg `-0.5045` n `23`; metal avg `-0.0948` n `18`; unknown avg `0.8506` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
