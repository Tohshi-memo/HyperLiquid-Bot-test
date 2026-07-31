# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T11:52:36.374730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0594` n `12`; crypto_alt avg `-0.0374` n `230`; crypto_major avg `0.0134` n `8`; equity avg `0.0856` n `102`; fx avg `-0.032` n `6`; index avg `0.0134` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.0074` n `780`
- 1h: commodity avg `0.2303` n `12`; crypto_alt avg `-0.2272` n `230`; crypto_major avg `-0.0731` n `8`; equity avg `0.1035` n `102`; fx avg `-0.0011` n `6`; index avg `-0.0203` n `25`; metal avg `-0.0802` n `20`; unknown avg `2.0447` n `780`
- 4h: commodity avg `0.6077` n `12`; crypto_alt avg `-0.6596` n `230`; crypto_major avg `-0.2988` n `8`; equity avg `0.3418` n `102`; fx avg `0.0358` n `6`; index avg `-0.0113` n `25`; metal avg `-0.1981` n `20`; unknown avg `0.6723` n `779`
- 24h: commodity avg `0.5017` n `12`; crypto_alt avg `-0.6236` n `230`; crypto_major avg `-0.4247` n `8`; equity avg `6.9117` n `102`; fx avg `-0.0948` n `6`; index avg `0.9778` n `25`; metal avg `-0.0314` n `20`; unknown avg `0.7503` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
