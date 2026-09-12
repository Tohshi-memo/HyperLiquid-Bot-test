# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T20:37:41.304848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.0353` n `233`; crypto_major avg `0.001` n `8`; equity avg `-0.0506` n `136`; fx avg `-0.0026` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0044` n `20`; unknown avg `20.1166` n `832`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.2329` n `233`; crypto_major avg `0.1755` n `8`; equity avg `-0.1073` n `136`; fx avg `-0.0004` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0101` n `20`; unknown avg `20.9456` n `830`
- 4h: commodity avg `0.0436` n `12`; crypto_alt avg `-0.3299` n `233`; crypto_major avg `-0.3562` n `8`; equity avg `-0.355` n `136`; fx avg `-0.004` n `6`; index avg `-0.0497` n `26`; metal avg `-0.0173` n `20`; unknown avg `7.3932` n `782`
- 24h: commodity avg `-0.1537` n `12`; crypto_alt avg `0.8624` n `233`; crypto_major avg `-0.3681` n `8`; equity avg `-0.2863` n `136`; fx avg `-0.0249` n `6`; index avg `0.0027` n `26`; metal avg `-0.0049` n `20`; unknown avg `2.5332` n `736`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
