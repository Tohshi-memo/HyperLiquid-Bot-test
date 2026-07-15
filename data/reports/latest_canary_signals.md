# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T19:59:33.067585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.36` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1223` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.1107` n `230`; crypto_major avg `-0.1123` n `8`; equity avg `0.0801` n `94`; fx avg `0.0066` n `6`; index avg `0.0246` n `25`; metal avg `0.022` n `20`; unknown avg `-0.1048` n `768`
- 1h: commodity avg `0.1355` n `12`; crypto_alt avg `-0.2836` n `230`; crypto_major avg `-0.3837` n `8`; equity avg `0.2496` n `94`; fx avg `0.0082` n `6`; index avg `0.0574` n `25`; metal avg `-0.0418` n `20`; unknown avg `-0.0902` n `768`
- 4h: commodity avg `0.3772` n `12`; crypto_alt avg `-0.6824` n `230`; crypto_major avg `-1.0162` n `8`; equity avg `0.3756` n `94`; fx avg `0.076` n `6`; index avg `0.1061` n `25`; metal avg `0.2496` n `20`; unknown avg `0.0045` n `768`
- 24h: commodity avg `0.1709` n `12`; crypto_alt avg `0.2018` n `230`; crypto_major avg `0.4336` n `8`; equity avg `-0.4419` n `93`; fx avg `0.2162` n `6`; index avg `-0.163` n `25`; metal avg `0.1355` n `20`; unknown avg `0.1858` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
