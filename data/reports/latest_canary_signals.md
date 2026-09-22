# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T02:52:28.645580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.5212` n `234`; crypto_major avg `-0.3595` n `8`; equity avg `0.0376` n `140`; fx avg `0.0058` n `6`; index avg `0.0034` n `26`; metal avg `-0.0542` n `20`; unknown avg `-0.0392` n `944`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.1379` n `234`; crypto_major avg `-0.2219` n `8`; equity avg `0.1486` n `140`; fx avg `0.0076` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0222` n `20`; unknown avg `0.3124` n `942`
- 4h: commodity avg `0.1954` n `12`; crypto_alt avg `0.1371` n `234`; crypto_major avg `-0.9558` n `8`; equity avg `0.2874` n `140`; fx avg `-0.1448` n `6`; index avg `0.002` n `26`; metal avg `-0.1049` n `20`; unknown avg `0.8978` n `936`
- 24h: commodity avg `-0.126` n `12`; crypto_alt avg `3.8881` n `234`; crypto_major avg `4.3288` n `8`; equity avg `2.4863` n `140`; fx avg `-0.2096` n `6`; index avg `0.4899` n `26`; metal avg `-0.0264` n `20`; unknown avg `11.0249` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
