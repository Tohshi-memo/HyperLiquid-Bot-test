# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T18:42:04.030014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1087` n `12`; crypto_alt avg `-0.3376` n `230`; crypto_major avg `-0.4101` n `8`; equity avg `-0.0283` n `102`; fx avg `0.0044` n `6`; index avg `0.0087` n `25`; metal avg `0.0268` n `20`; unknown avg `0.0842` n `780`
- 1h: commodity avg `0.02` n `12`; crypto_alt avg `-0.3633` n `230`; crypto_major avg `-0.3995` n `8`; equity avg `-0.2622` n `102`; fx avg `0.0764` n `6`; index avg `-0.0213` n `25`; metal avg `0.0583` n `20`; unknown avg `7.5063` n `780`
- 4h: commodity avg `-0.0988` n `12`; crypto_alt avg `0.196` n `230`; crypto_major avg `-0.3264` n `8`; equity avg `0.3866` n `102`; fx avg `0.107` n `6`; index avg `0.1597` n `25`; metal avg `0.2278` n `20`; unknown avg `9.0092` n `780`
- 24h: commodity avg `0.1765` n `12`; crypto_alt avg `-0.3103` n `230`; crypto_major avg `-1.9528` n `8`; equity avg `0.8023` n `102`; fx avg `0.2384` n `6`; index avg `0.3489` n `25`; metal avg `-0.2611` n `20`; unknown avg `0.3768` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
