# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T17:07:26.925156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0575` n `12`; crypto_alt avg `0.1465` n `230`; crypto_major avg `0.1641` n `8`; equity avg `0.2565` n `94`; fx avg `0.0238` n `6`; index avg `0.029` n `25`; metal avg `0.0273` n `20`; unknown avg `-0.0312` n `768`
- 1h: commodity avg `0.074` n `12`; crypto_alt avg `-0.0606` n `230`; crypto_major avg `-0.1136` n `8`; equity avg `0.2976` n `94`; fx avg `0.0497` n `6`; index avg `0.0282` n `25`; metal avg `-0.0699` n `20`; unknown avg `-0.0541` n `768`
- 4h: commodity avg `0.0206` n `12`; crypto_alt avg `-1.0454` n `230`; crypto_major avg `-0.9276` n `8`; equity avg `-2.3257` n `93`; fx avg `0.1241` n `6`; index avg `-0.4409` n `25`; metal avg `-0.4308` n `20`; unknown avg `0.0988` n `768`
- 24h: commodity avg `0.059` n `12`; crypto_alt avg `0.1716` n `230`; crypto_major avg `1.1448` n `8`; equity avg `-1.427` n `92`; fx avg `0.1864` n `6`; index avg `-0.3204` n `25`; metal avg `-0.248` n `20`; unknown avg `0.2867` n `746`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
