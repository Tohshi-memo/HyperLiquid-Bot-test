# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T22:22:25.543185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1525` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.0202` n `234`; crypto_major avg `-0.127` n `8`; equity avg `0.0034` n `140`; fx avg `-0.0002` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.794` n `935`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `-0.2656` n `234`; crypto_major avg `-0.513` n `8`; equity avg `-0.0023` n `140`; fx avg `0.0093` n `6`; index avg `0.0033` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.306` n `933`
- 4h: commodity avg `0.0026` n `12`; crypto_alt avg `-0.9511` n `234`; crypto_major avg `-1.1452` n `8`; equity avg `0.0793` n `140`; fx avg `-0.0289` n `6`; index avg `0.0073` n `26`; metal avg `0.0043` n `20`; unknown avg `55.6439` n `911`
- 24h: commodity avg `0.1062` n `12`; crypto_alt avg `0.1568` n `234`; crypto_major avg `-0.9506` n `8`; equity avg `-0.0742` n `140`; fx avg `-0.0564` n `6`; index avg `0.02` n `26`; metal avg `-0.018` n `20`; unknown avg `6.4395` n `838`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
