# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T13:37:26.664185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6397` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2355` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `-0.7553` n `232`; crypto_major avg `-0.5078` n `8`; equity avg `-0.0174` n `134`; fx avg `-0.029` n `6`; index avg `-0.046` n `26`; metal avg `-0.1193` n `20`; unknown avg `1.151` n `797`
- 1h: commodity avg `-0.0742` n `12`; crypto_alt avg `-0.994` n `232`; crypto_major avg `-0.6515` n `8`; equity avg `0.0998` n `134`; fx avg `-0.0191` n `6`; index avg `0.0084` n `26`; metal avg `-0.0396` n `20`; unknown avg `0.7544` n `795`
- 4h: commodity avg `-0.2416` n `12`; crypto_alt avg `-1.5682` n `232`; crypto_major avg `-1.1854` n `8`; equity avg `0.4543` n `134`; fx avg `-0.029` n `6`; index avg `0.0501` n `26`; metal avg `-0.005` n `20`; unknown avg `0.8659` n `789`
- 24h: commodity avg `0.028` n `12`; crypto_alt avg `-1.5361` n `232`; crypto_major avg `-1.9244` n `8`; equity avg `0.2391` n `134`; fx avg `-0.1448` n `6`; index avg `-0.0208` n `26`; metal avg `0.077` n `20`; unknown avg `1.2567` n `710`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
