# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T05:52:28.121830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0466` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `0.1285` n `234`; crypto_major avg `0.0597` n `8`; equity avg `0.0281` n `140`; fx avg `-0.0007` n `6`; index avg `-0.0016` n `26`; metal avg `0.0034` n `20`; unknown avg `5.0298` n `943`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.0611` n `234`; crypto_major avg `0.0113` n `8`; equity avg `0.0367` n `140`; fx avg `-0.0067` n `6`; index avg `-0.003` n `26`; metal avg `0.0063` n `20`; unknown avg `43.3004` n `941`
- 4h: commodity avg `0.0911` n `12`; crypto_alt avg `-1.2267` n `234`; crypto_major avg `-1.1229` n `8`; equity avg `-0.426` n `140`; fx avg `-0.0025` n `6`; index avg `-0.0763` n `26`; metal avg `-0.0419` n `20`; unknown avg `6.6028` n `925`
- 24h: commodity avg `0.2159` n `12`; crypto_alt avg `0.1986` n `234`; crypto_major avg `-1.9527` n `8`; equity avg `-0.2009` n `140`; fx avg `-0.0725` n `6`; index avg `-0.032` n `26`; metal avg `-0.0049` n `20`; unknown avg `4.7794` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
