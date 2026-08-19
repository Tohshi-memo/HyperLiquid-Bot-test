# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T13:07:29.268902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `-0.1077` n `230`; crypto_major avg `-0.0839` n `8`; equity avg `-0.0414` n `120`; fx avg `0.0105` n `6`; index avg `-0.0063` n `25`; metal avg `0.0383` n `20`; unknown avg `0.0533` n `792`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.214` n `230`; crypto_major avg `0.5079` n `8`; equity avg `1.2359` n `120`; fx avg `0.0009` n `6`; index avg `0.1676` n `25`; metal avg `0.355` n `20`; unknown avg `-0.03` n `792`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.335` n `230`; crypto_major avg `0.61` n `8`; equity avg `0.5194` n `120`; fx avg `-0.0483` n `6`; index avg `0.1068` n `25`; metal avg `0.46` n `20`; unknown avg `0.254` n `791`
- 24h: commodity avg `0.3444` n `12`; crypto_alt avg `0.5253` n `230`; crypto_major avg `1.0888` n `8`; equity avg `-0.5783` n `120`; fx avg `-0.2163` n `6`; index avg `-0.0304` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0227` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
