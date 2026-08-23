# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T12:52:31.279361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `0.1975` n `230`; crypto_major avg `0.0951` n `8`; equity avg `0.0147` n `121`; fx avg `-0.0014` n `6`; index avg `0.0003` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.1069` n `795`
- 1h: commodity avg `0.0073` n `12`; crypto_alt avg `0.1665` n `230`; crypto_major avg `-0.2352` n `8`; equity avg `0.0424` n `121`; fx avg `0.0016` n `6`; index avg `0.0092` n `25`; metal avg `0.009` n `20`; unknown avg `1.862` n `795`
- 4h: commodity avg `0.0207` n `12`; crypto_alt avg `2.1042` n `230`; crypto_major avg `0.89` n `8`; equity avg `0.2426` n `121`; fx avg `-0.0046` n `6`; index avg `0.0386` n `25`; metal avg `0.0365` n `20`; unknown avg `2.4992` n `794`
- 24h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.2338` n `230`; crypto_major avg `0.3877` n `8`; equity avg `0.453` n `121`; fx avg `0.0338` n `6`; index avg `0.0429` n `25`; metal avg `0.0561` n `20`; unknown avg `6.5233` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
