# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T09:22:28.983571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0422` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0876` n `12`; crypto_alt avg `0.0418` n `230`; crypto_major avg `0.0285` n `8`; equity avg `0.0933` n `94`; fx avg `-0.0044` n `6`; index avg `0.0009` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0095` n `768`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `0.2434` n `230`; crypto_major avg `0.2695` n `8`; equity avg `0.3028` n `94`; fx avg `0.0094` n `6`; index avg `0.0742` n `25`; metal avg `0.0558` n `20`; unknown avg `0.1371` n `762`
- 4h: commodity avg `-0.0568` n `12`; crypto_alt avg `-1.101` n `230`; crypto_major avg `-1.17` n `8`; equity avg `-0.8562` n `94`; fx avg `-0.0555` n `6`; index avg `-0.1278` n `25`; metal avg `-0.0505` n `20`; unknown avg `-0.1014` n `746`
- 24h: commodity avg `-0.1855` n `12`; crypto_alt avg `-0.8662` n `230`; crypto_major avg `-1.1401` n `8`; equity avg `-2.7178` n `93`; fx avg `0.0554` n `6`; index avg `-0.4516` n `25`; metal avg `-0.0387` n `20`; unknown avg `-0.1596` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
