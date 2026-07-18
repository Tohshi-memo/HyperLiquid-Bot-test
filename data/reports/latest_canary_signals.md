# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T15:10:11.083594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0334` n `12`; crypto_alt avg `0.0086` n `230`; crypto_major avg `-0.059` n `8`; equity avg `-0.0136` n `96`; fx avg `0.0055` n `6`; index avg `0.0053` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0325` n `770`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `0.2874` n `230`; crypto_major avg `0.2785` n `8`; equity avg `0.0134` n `96`; fx avg `-0.0009` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0173` n `20`; unknown avg `0.0047` n `770`
- 4h: commodity avg `-0.0163` n `12`; crypto_alt avg `0.0232` n `230`; crypto_major avg `0.1359` n `8`; equity avg `-0.0963` n `96`; fx avg `-0.0004` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0363` n `20`; unknown avg `-0.0553` n `770`
- 24h: commodity avg `0.6201` n `12`; crypto_alt avg `-0.0331` n `230`; crypto_major avg `0.9413` n `8`; equity avg `0.4932` n `96`; fx avg `-0.0115` n `6`; index avg `0.1517` n `25`; metal avg `0.1094` n `20`; unknown avg `0.1352` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
