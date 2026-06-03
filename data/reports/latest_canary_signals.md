# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T16:07:30.162993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `-0.6059` n `228`; crypto_major avg `-0.2799` n `8`; equity avg `-0.1379` n `73`; fx avg `-0.0102` n `6`; index avg `0.0053` n `23`; metal avg `-0.1032` n `18`; unknown avg `-0.3689` n `419`
- 1h: commodity avg `0.1737` n `12`; crypto_alt avg `-1.0551` n `228`; crypto_major avg `-0.6117` n `8`; equity avg `-0.6039` n `73`; fx avg `-0.0032` n `6`; index avg `-0.236` n `23`; metal avg `-0.4131` n `18`; unknown avg `-0.4693` n `419`
- 4h: commodity avg `-0.1076` n `12`; crypto_alt avg `-0.6297` n `228`; crypto_major avg `-1.3014` n `8`; equity avg `-2.1008` n `73`; fx avg `-0.005` n `6`; index avg `-0.6461` n `23`; metal avg `-1.1773` n `18`; unknown avg `0.0531` n `419`
- 24h: commodity avg `1.2092` n `12`; crypto_alt avg `1.1297` n `228`; crypto_major avg `-2.4346` n `8`; equity avg `-1.9859` n `72`; fx avg `0.0033` n `6`; index avg `-0.3039` n `23`; metal avg `-2.253` n `18`; unknown avg `0.4201` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
