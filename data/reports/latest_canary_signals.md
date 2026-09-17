# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T07:52:30.475625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0568` n `12`; crypto_alt avg `-0.0131` n `234`; crypto_major avg `-0.0594` n `8`; equity avg `-0.0538` n `137`; fx avg `0.0115` n `6`; index avg `-0.0125` n `27`; metal avg `0.0048` n `20`; unknown avg `0.2622` n `921`
- 1h: commodity avg `0.0937` n `12`; crypto_alt avg `0.1542` n `234`; crypto_major avg `0.0742` n `8`; equity avg `0.272` n `137`; fx avg `0.0133` n `6`; index avg `0.0411` n `27`; metal avg `0.1869` n `20`; unknown avg `0.3016` n `919`
- 4h: commodity avg `-0.1314` n `12`; crypto_alt avg `0.7282` n `234`; crypto_major avg `0.1189` n `8`; equity avg `0.3069` n `137`; fx avg `0.0248` n `6`; index avg `0.0468` n `27`; metal avg `0.2298` n `20`; unknown avg `0.2263` n `891`
- 24h: commodity avg `-0.4358` n `12`; crypto_alt avg `3.2494` n `234`; crypto_major avg `1.7224` n `8`; equity avg `1.1855` n `137`; fx avg `0.08` n `6`; index avg `0.1069` n `27`; metal avg `0.0423` n `20`; unknown avg `0.6803` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
