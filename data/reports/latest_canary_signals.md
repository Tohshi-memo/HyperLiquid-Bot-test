# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T04:22:26.008319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.1124` n `234`; crypto_major avg `0.0294` n `8`; equity avg `0.0072` n `140`; fx avg `-0.0007` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.1016` n `942`
- 1h: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.1505` n `234`; crypto_major avg `0.0275` n `8`; equity avg `0.0137` n `140`; fx avg `-0.0025` n `6`; index avg `0.0068` n `26`; metal avg `-0.0091` n `20`; unknown avg `-0.2879` n `914`
- 4h: commodity avg `-0.0297` n `12`; crypto_alt avg `0.2178` n `234`; crypto_major avg `0.3864` n `8`; equity avg `-0.1431` n `140`; fx avg `-0.0024` n `6`; index avg `-0.0264` n `26`; metal avg `-0.0364` n `20`; unknown avg `0.2753` n `914`
- 24h: commodity avg `0.0857` n `12`; crypto_alt avg `4.2773` n `234`; crypto_major avg `5.1187` n `8`; equity avg `0.7077` n `140`; fx avg `0.0301` n `6`; index avg `0.0135` n `26`; metal avg `0.1191` n `20`; unknown avg `2.5155` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
