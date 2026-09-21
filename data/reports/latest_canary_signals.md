# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T02:07:31.152683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0397` n `12`; crypto_alt avg `-0.4016` n `234`; crypto_major avg `-0.1103` n `8`; equity avg `-0.0288` n `140`; fx avg `-0.0037` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0131` n `20`; unknown avg `0.0209` n `942`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `-1.2536` n `234`; crypto_major avg `-0.9887` n `8`; equity avg `-0.2297` n `140`; fx avg `-0.014` n `6`; index avg `-0.016` n `26`; metal avg `-0.065` n `20`; unknown avg `4.0305` n `942`
- 4h: commodity avg `-0.4718` n `12`; crypto_alt avg `-0.5886` n `234`; crypto_major avg `0.3861` n `8`; equity avg `0.6197` n `140`; fx avg `-0.0125` n `6`; index avg `0.1234` n `26`; metal avg `0.0539` n `20`; unknown avg `8.579` n `919`
- 24h: commodity avg `-0.6` n `12`; crypto_alt avg `0.1182` n `234`; crypto_major avg `0.798` n `8`; equity avg `0.6045` n `140`; fx avg `0.0033` n `6`; index avg `0.1033` n `26`; metal avg `0.0839` n `20`; unknown avg `3.1491` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
