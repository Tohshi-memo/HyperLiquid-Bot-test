# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T19:52:26.282483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `0.0422` n `230`; crypto_major avg `0.1623` n `8`; equity avg `0.0129` n `102`; fx avg `0.0015` n `6`; index avg `0.0082` n `25`; metal avg `0.008` n `20`; unknown avg `0.0133` n `783`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.0069` n `230`; crypto_major avg `0.0639` n `8`; equity avg `0.0882` n `102`; fx avg `0.0585` n `6`; index avg `0.008` n `25`; metal avg `0.0287` n `20`; unknown avg `-0.0368` n `782`
- 4h: commodity avg `-0.1261` n `12`; crypto_alt avg `0.1985` n `230`; crypto_major avg `0.8114` n `8`; equity avg `0.4577` n `102`; fx avg `0.0746` n `6`; index avg `0.059` n `25`; metal avg `0.0964` n `20`; unknown avg `0.5015` n `782`
- 24h: commodity avg `-1.331` n `12`; crypto_alt avg `1.4651` n `230`; crypto_major avg `2.1363` n `8`; equity avg `1.7106` n `102`; fx avg `-0.07` n `6`; index avg `0.331` n `25`; metal avg `0.3375` n `20`; unknown avg `1.6224` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
