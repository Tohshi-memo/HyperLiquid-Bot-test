# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T21:22:28.121617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3055` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.2476` n `233`; crypto_major avg `-0.2425` n `8`; equity avg `-0.0844` n `134`; fx avg `0.0088` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0092` n `20`; unknown avg `4.6801` n `797`
- 1h: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.2391` n `233`; crypto_major avg `-0.1429` n `8`; equity avg `-0.1135` n `134`; fx avg `0.0019` n `6`; index avg `0.0061` n `26`; metal avg `0.0436` n `20`; unknown avg `3.592` n `767`
- 4h: commodity avg `0.1684` n `12`; crypto_alt avg `-1.7673` n `233`; crypto_major avg `-1.3159` n `8`; equity avg `-0.4024` n `134`; fx avg `-0.0092` n `6`; index avg `-0.0104` n `26`; metal avg `-0.2191` n `20`; unknown avg `1.7778` n `745`
- 24h: commodity avg `0.1135` n `12`; crypto_alt avg `-1.6554` n `233`; crypto_major avg `-1.1562` n `8`; equity avg `-0.4908` n `134`; fx avg `-0.0179` n `6`; index avg `-0.115` n `26`; metal avg `0.4949` n `20`; unknown avg `151.5721` n `699`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
