# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T19:07:30.857506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.5763` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4876` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0195` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0341` n `12`; crypto_alt avg `0.838` n `233`; crypto_major avg `0.7314` n `8`; equity avg `0.2396` n `137`; fx avg `0.0017` n `6`; index avg `0.0125` n `27`; metal avg `-0.0142` n `20`; unknown avg `2.5706` n `916`
- 1h: commodity avg `-0.0666` n `12`; crypto_alt avg `-1.2588` n `233`; crypto_major avg `-1.5001` n `8`; equity avg `-0.2411` n `137`; fx avg `0.019` n `6`; index avg `-0.0125` n `27`; metal avg `0.0762` n `20`; unknown avg `14.7766` n `916`
- 4h: commodity avg `0.0051` n `12`; crypto_alt avg `-0.8341` n `233`; crypto_major avg `-1.0066` n `8`; equity avg `-0.2264` n `137`; fx avg `0.0087` n `6`; index avg `0.0129` n `27`; metal avg `0.2718` n `20`; unknown avg `2.0604` n `901`
- 24h: commodity avg `0.608` n `12`; crypto_alt avg `-3.8581` n `233`; crypto_major avg `-4.4071` n `8`; equity avg `-1.4558` n `137`; fx avg `0.2429` n `6`; index avg `-0.152` n `27`; metal avg `0.142` n `20`; unknown avg `3.2702` n `831`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
