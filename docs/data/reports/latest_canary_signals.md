# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T02:07:29.817952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `0.0298` n `234`; crypto_major avg `0.0249` n `8`; equity avg `0.0537` n `140`; fx avg `-0.011` n `6`; index avg `0.0031` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.0893` n `942`
- 1h: commodity avg `0.0247` n `12`; crypto_alt avg `0.0591` n `234`; crypto_major avg `-0.0788` n `8`; equity avg `-0.1233` n `140`; fx avg `-0.016` n `6`; index avg `-0.0212` n `26`; metal avg `-0.1244` n `20`; unknown avg `-0.2038` n `942`
- 4h: commodity avg `0.2603` n `12`; crypto_alt avg `0.447` n `234`; crypto_major avg `-0.9197` n `8`; equity avg `0.2477` n `140`; fx avg `-0.1661` n `6`; index avg `0.0292` n `26`; metal avg `-0.0304` n `20`; unknown avg `1.0265` n `936`
- 24h: commodity avg `-0.1708` n `12`; crypto_alt avg `4.5938` n `234`; crypto_major avg `4.8608` n `8`; equity avg `2.4062` n `140`; fx avg `-0.2614` n `6`; index avg `0.5135` n `26`; metal avg `-0.0671` n `20`; unknown avg `11.8017` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
