# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T20:22:36.036349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `-0.1175` n `230`; crypto_major avg `-0.0117` n `8`; equity avg `-0.0103` n `112`; fx avg `-0.0062` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0214` n `20`; unknown avg `0.027` n `782`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `-0.2246` n `230`; crypto_major avg `0.0318` n `8`; equity avg `0.0436` n `112`; fx avg `-0.0082` n `6`; index avg `-0.0141` n `25`; metal avg `-0.1295` n `20`; unknown avg `-0.0771` n `782`
- 4h: commodity avg `-0.2976` n `12`; crypto_alt avg `-0.3359` n `230`; crypto_major avg `-0.3407` n `8`; equity avg `0.0589` n `112`; fx avg `-0.0153` n `6`; index avg `0.0215` n `25`; metal avg `-0.025` n `20`; unknown avg `-0.2364` n `782`
- 24h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.1338` n `230`; crypto_major avg `0.063` n `8`; equity avg `2.0691` n `112`; fx avg `-0.1579` n `6`; index avg `0.1041` n `25`; metal avg `0.3272` n `20`; unknown avg `-0.0047` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
