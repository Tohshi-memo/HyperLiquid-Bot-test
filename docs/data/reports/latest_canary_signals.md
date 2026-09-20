# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T04:22:24.403533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5858` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5531` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.1968` n `234`; crypto_major avg `-0.2211` n `8`; equity avg `-0.0371` n `140`; fx avg `-0.0005` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0097` n `20`; unknown avg `0.4307` n `943`
- 1h: commodity avg `0.0402` n `12`; crypto_alt avg `-0.3141` n `234`; crypto_major avg `-0.3328` n `8`; equity avg `-0.0662` n `140`; fx avg `-0.0049` n `6`; index avg `-0.0044` n `26`; metal avg `0.0023` n `20`; unknown avg `60.3763` n `935`
- 4h: commodity avg `0.2007` n `12`; crypto_alt avg `-1.6673` n `234`; crypto_major avg `-1.6253` n `8`; equity avg `-0.3855` n `140`; fx avg `0.0067` n `6`; index avg `-0.0722` n `26`; metal avg `-0.0395` n `20`; unknown avg `6.3778` n `935`
- 24h: commodity avg `0.2438` n `12`; crypto_alt avg `-0.958` n `234`; crypto_major avg `-2.2991` n `8`; equity avg `-0.2951` n `140`; fx avg `-0.058` n `6`; index avg `-0.0373` n `26`; metal avg `-0.0174` n `20`; unknown avg `6.0916` n `826`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
