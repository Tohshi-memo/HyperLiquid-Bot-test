# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T14:22:25.954775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `0.2416` n `234`; crypto_major avg `0.271` n `8`; equity avg `-0.0091` n `140`; fx avg `0.0` n `6`; index avg `-0.0011` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.0867` n `942`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `0.4336` n `234`; crypto_major avg `0.3502` n `8`; equity avg `0.0376` n `140`; fx avg `0.0096` n `6`; index avg `0.0027` n `26`; metal avg `0.0109` n `20`; unknown avg `1.2108` n `938`
- 4h: commodity avg `0.0311` n `12`; crypto_alt avg `0.7249` n `234`; crypto_major avg `0.767` n `8`; equity avg `0.0343` n `140`; fx avg `-0.029` n `6`; index avg `-0.0042` n `26`; metal avg `0.0249` n `20`; unknown avg `0.2344` n `932`
- 24h: commodity avg `-0.1823` n `12`; crypto_alt avg `3.2589` n `234`; crypto_major avg `2.1095` n `8`; equity avg `0.8657` n `140`; fx avg `-0.0447` n `6`; index avg `0.1272` n `26`; metal avg `0.1126` n `20`; unknown avg `1.4132` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
