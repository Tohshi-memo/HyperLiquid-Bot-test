# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T20:07:28.107560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `0.072` n `234`; crypto_major avg `-0.1265` n `8`; equity avg `0.0084` n `140`; fx avg `-0.001` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0063` n `20`; unknown avg `16.453` n `935`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `0.5523` n `234`; crypto_major avg `0.3018` n `8`; equity avg `0.0641` n `140`; fx avg `0.0061` n `6`; index avg `-0.0049` n `26`; metal avg `0.0095` n `20`; unknown avg `17.7583` n `935`
- 4h: commodity avg `0.0256` n `12`; crypto_alt avg `1.8232` n `234`; crypto_major avg `1.0431` n `8`; equity avg `0.1458` n `140`; fx avg `0.0028` n `6`; index avg `0.022` n `26`; metal avg `-0.0005` n `20`; unknown avg `14.5977` n `907`
- 24h: commodity avg `0.3975` n `12`; crypto_alt avg `0.5162` n `234`; crypto_major avg `-0.2813` n `8`; equity avg `-0.088` n `140`; fx avg `-0.0375` n `6`; index avg `-0.0459` n `26`; metal avg `-0.0344` n `20`; unknown avg `3.6614` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
