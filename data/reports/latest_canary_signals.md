# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T08:22:26.275588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.0082` n `230`; crypto_major avg `-0.0198` n `8`; equity avg `-0.1034` n `108`; fx avg `-0.0165` n `6`; index avg `-0.0222` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0803` n `782`
- 1h: commodity avg `0.0759` n `12`; crypto_alt avg `-0.0857` n `230`; crypto_major avg `-0.2061` n `8`; equity avg `-0.373` n `108`; fx avg `0.0117` n `6`; index avg `-0.0607` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.077` n `782`
- 4h: commodity avg `0.2345` n `12`; crypto_alt avg `0.1872` n `230`; crypto_major avg `-0.0914` n `8`; equity avg `-0.5197` n `108`; fx avg `0.0901` n `6`; index avg `-0.0886` n `25`; metal avg `-0.0194` n `20`; unknown avg `-0.0739` n `750`
- 24h: commodity avg `-0.1184` n `12`; crypto_alt avg `0.1556` n `230`; crypto_major avg `-0.3849` n `8`; equity avg `-1.6675` n `108`; fx avg `0.0146` n `6`; index avg `-0.336` n `25`; metal avg `0.2833` n `20`; unknown avg `0.7588` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
