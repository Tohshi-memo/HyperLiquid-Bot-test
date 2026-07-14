# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T06:37:30.543400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `12`; crypto_alt avg `0.0007` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `0.0766` n `92`; fx avg `0.0023` n `6`; index avg `-0.0163` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0477` n `766`
- 1h: commodity avg `0.1916` n `12`; crypto_alt avg `0.0742` n `230`; crypto_major avg `-0.0791` n `8`; equity avg `0.0251` n `92`; fx avg `0.0169` n `6`; index avg `-0.0422` n `25`; metal avg `-0.0453` n `20`; unknown avg `-0.0434` n `750`
- 4h: commodity avg `0.1763` n `12`; crypto_alt avg `0.6439` n `230`; crypto_major avg `0.465` n `8`; equity avg `1.1561` n `92`; fx avg `-0.0073` n `6`; index avg `0.2778` n `25`; metal avg `0.2258` n `20`; unknown avg `0.0162` n `750`
- 24h: commodity avg `1.1079` n `12`; crypto_alt avg `-0.4024` n `230`; crypto_major avg `-0.4001` n `8`; equity avg `-0.0492` n `92`; fx avg `-0.1333` n `6`; index avg `-0.015` n `25`; metal avg `0.1062` n `20`; unknown avg `-0.2132` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
