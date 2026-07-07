# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T10:37:29.952296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.0294` n `229`; crypto_major avg `-0.1579` n `8`; equity avg `-0.1085` n `91`; fx avg `-0.0098` n `6`; index avg `-0.0235` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0469` n `763`
- 1h: commodity avg `-0.0684` n `12`; crypto_alt avg `0.3939` n `229`; crypto_major avg `0.1112` n `8`; equity avg `0.0255` n `91`; fx avg `-0.0476` n `6`; index avg `-0.0165` n `25`; metal avg `0.0922` n `20`; unknown avg `0.0376` n `761`
- 4h: commodity avg `-0.0108` n `12`; crypto_alt avg `0.1785` n `229`; crypto_major avg `-0.0016` n `8`; equity avg `-0.2101` n `91`; fx avg `-0.1297` n `6`; index avg `-0.0305` n `25`; metal avg `0.2296` n `20`; unknown avg `-0.3871` n `757`
- 24h: commodity avg `0.4004` n `12`; crypto_alt avg `0.5358` n `229`; crypto_major avg `-0.2436` n `8`; equity avg `-1.6175` n `90`; fx avg `-0.1307` n `6`; index avg `-0.3809` n `25`; metal avg `-0.2545` n `20`; unknown avg `-0.4659` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
