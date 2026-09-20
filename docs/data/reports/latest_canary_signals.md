# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T04:52:34.347915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5269` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4914` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.1035` n `234`; crypto_major avg `-0.1068` n `8`; equity avg `-0.0383` n `140`; fx avg `0.0` n `6`; index avg `-0.0087` n `26`; metal avg `0.0119` n `20`; unknown avg `-0.1081` n `943`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `0.0281` n `234`; crypto_major avg `-0.0727` n `8`; equity avg `-0.0846` n `140`; fx avg `0.0023` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0084` n `20`; unknown avg `16.765` n `925`
- 4h: commodity avg `0.2042` n `12`; crypto_alt avg `-1.7019` n `234`; crypto_major avg `-1.5568` n `8`; equity avg `-0.4468` n `140`; fx avg `-0.0006` n `6`; index avg `-0.0654` n `26`; metal avg `-0.0299` n `20`; unknown avg `0.2308` n `925`
- 24h: commodity avg `0.2392` n `12`; crypto_alt avg `-0.0068` n `234`; crypto_major avg `-1.6321` n `8`; equity avg `-0.2416` n `140`; fx avg `-0.0457` n `6`; index avg `-0.0635` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.7959` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
