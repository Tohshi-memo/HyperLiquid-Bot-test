# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T02:07:32.978372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `0.0656` n `235`; crypto_major avg `0.1694` n `8`; equity avg `-0.0512` n `151`; fx avg `-0.0013` n `6`; index avg `-0.0168` n `26`; metal avg `0.0943` n `20`; unknown avg `0.3458` n `1133`
- 1h: commodity avg `-0.0352` n `13`; crypto_alt avg `1.3157` n `235`; crypto_major avg `1.2588` n `8`; equity avg `-0.1486` n `151`; fx avg `0.0066` n `6`; index avg `-0.0835` n `26`; metal avg `0.0129` n `20`; unknown avg `1.8568` n `1133`
- 4h: commodity avg `-0.1289` n `13`; crypto_alt avg `-1.8294` n `235`; crypto_major avg `-0.9294` n `8`; equity avg `-1.4126` n `151`; fx avg `0.0465` n `6`; index avg `-0.3157` n `26`; metal avg `-0.1135` n `20`; unknown avg `3.5817` n `1127`
- 24h: commodity avg `0.7129` n `13`; crypto_alt avg `-5.2283` n `235`; crypto_major avg `-3.2089` n `8`; equity avg `-4.756` n `151`; fx avg `-0.0774` n `6`; index avg `-0.6234` n `26`; metal avg `-0.3398` n `20`; unknown avg `0.4609` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2118`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.194`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1226`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1059`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.094`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0911`, n `666`, weak_sample_signal
