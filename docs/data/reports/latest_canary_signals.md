# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T21:22:27.415837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3971` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.7336` n `234`; crypto_major avg `-0.568` n `8`; equity avg `-0.0407` n `140`; fx avg `0.0014` n `6`; index avg `-0.0328` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.6597` n `943`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `-1.219` n `234`; crypto_major avg `-0.8616` n `8`; equity avg `-0.024` n `140`; fx avg `0.0021` n `6`; index avg `-0.0047` n `26`; metal avg `-0.009` n `20`; unknown avg `1.0706` n `941`
- 4h: commodity avg `0.0605` n `12`; crypto_alt avg `-1.5914` n `234`; crypto_major avg `-1.3926` n `8`; equity avg `0.0654` n `140`; fx avg `-0.0401` n `6`; index avg `0.0045` n `26`; metal avg `0.0129` n `20`; unknown avg `152.4017` n `919`
- 24h: commodity avg `0.0798` n `12`; crypto_alt avg `0.111` n `234`; crypto_major avg `-0.5618` n `8`; equity avg `-0.0643` n `140`; fx avg `-0.0816` n `6`; index avg `0.0015` n `26`; metal avg `-0.0064` n `20`; unknown avg `5.8475` n `820`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
