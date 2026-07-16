# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T09:26:42.788943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0424` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `0.0321` n `230`; crypto_major avg `0.0354` n `8`; equity avg `0.1083` n `94`; fx avg `-0.0055` n `6`; index avg `0.0079` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.0253` n `768`
- 1h: commodity avg `-0.0599` n `12`; crypto_alt avg `0.2336` n `230`; crypto_major avg `0.2764` n `8`; equity avg `0.3178` n `94`; fx avg `0.0084` n `6`; index avg `0.0812` n `25`; metal avg `0.0503` n `20`; unknown avg `0.1518` n `762`
- 4h: commodity avg `-0.0906` n `12`; crypto_alt avg `-1.1107` n `230`; crypto_major avg `-1.1633` n `8`; equity avg `-0.8421` n `94`; fx avg `-0.0566` n `6`; index avg `-0.1209` n `25`; metal avg `-0.056` n `20`; unknown avg `-0.0716` n `746`
- 24h: commodity avg `-0.2191` n `12`; crypto_alt avg `-0.8757` n `230`; crypto_major avg `-1.1333` n `8`; equity avg `-2.7056` n `93`; fx avg `0.0543` n `6`; index avg `-0.445` n `25`; metal avg `-0.0442` n `20`; unknown avg `-0.1294` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
