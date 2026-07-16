# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T18:22:29.822932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0011` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.1294` n `230`; crypto_major avg `0.1517` n `8`; equity avg `0.3265` n `94`; fx avg `-0.0033` n `6`; index avg `0.0567` n `25`; metal avg `0.0374` n `20`; unknown avg `0.0899` n `768`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.0946` n `230`; crypto_major avg `0.0312` n `8`; equity avg `0.1309` n `94`; fx avg `-0.0077` n `6`; index avg `0.0264` n `25`; metal avg `-0.0164` n `20`; unknown avg `0.3984` n `768`
- 4h: commodity avg `-0.525` n `12`; crypto_alt avg `-0.4704` n `230`; crypto_major avg `-1.142` n `8`; equity avg `-0.9355` n `94`; fx avg `-0.0738` n `6`; index avg `-0.1409` n `25`; metal avg `-0.138` n `20`; unknown avg `-0.2018` n `768`
- 24h: commodity avg `-0.2555` n `12`; crypto_alt avg `-1.0912` n `230`; crypto_major avg `-2.4555` n `8`; equity avg `-3.5328` n `94`; fx avg `-0.1649` n `6`; index avg `-0.4823` n `25`; metal avg `-0.7391` n `20`; unknown avg `-0.3055` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
