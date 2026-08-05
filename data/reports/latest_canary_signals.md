# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T21:37:36.185159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `-0.1777` n `230`; crypto_major avg `-0.1772` n `8`; equity avg `-0.123` n `108`; fx avg `-0.0005` n `6`; index avg `-0.0166` n `25`; metal avg `0.0027` n `20`; unknown avg `0.0344` n `782`
- 1h: commodity avg `0.0947` n `12`; crypto_alt avg `-0.3808` n `230`; crypto_major avg `-0.4606` n `8`; equity avg `-0.341` n `108`; fx avg `0.0029` n `6`; index avg `-0.0355` n `25`; metal avg `0.0105` n `20`; unknown avg `0.2079` n `782`
- 4h: commodity avg `0.13` n `12`; crypto_alt avg `-0.315` n `230`; crypto_major avg `-0.411` n `8`; equity avg `-1.2756` n `108`; fx avg `0.0018` n `6`; index avg `-0.1213` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0064` n `782`
- 24h: commodity avg `0.0564` n `12`; crypto_alt avg `0.2677` n `230`; crypto_major avg `0.5104` n `8`; equity avg `-0.9167` n `108`; fx avg `-0.0517` n `6`; index avg `-0.14` n `25`; metal avg `0.8049` n `20`; unknown avg `0.6918` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
