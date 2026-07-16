# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T17:57:28.944860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1334` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0511` n `12`; crypto_alt avg `-0.3181` n `230`; crypto_major avg `-0.3644` n `8`; equity avg `-0.2954` n `94`; fx avg `0.0107` n `6`; index avg `-0.0534` n `25`; metal avg `-0.0089` n `20`; unknown avg `-0.1985` n `768`
- 1h: commodity avg `-0.0953` n `12`; crypto_alt avg `-0.6404` n `230`; crypto_major avg `-0.9858` n `8`; equity avg `-0.5014` n `94`; fx avg `-0.0047` n `6`; index avg `-0.0909` n `25`; metal avg `-0.1707` n `20`; unknown avg `-0.3179` n `768`
- 4h: commodity avg `-0.4967` n `12`; crypto_alt avg `-0.5709` n `230`; crypto_major avg `-1.2436` n `8`; equity avg `-1.2334` n `94`; fx avg `-0.0587` n `6`; index avg `-0.1102` n `25`; metal avg `-0.2114` n `20`; unknown avg `-0.3916` n `768`
- 24h: commodity avg `-0.2617` n `12`; crypto_alt avg `-1.2328` n `230`; crypto_major avg `-2.5729` n `8`; equity avg `-3.7699` n `94`; fx avg `-0.1509` n `6`; index avg `-0.4819` n `25`; metal avg `-0.6372` n `20`; unknown avg `-0.3732` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
