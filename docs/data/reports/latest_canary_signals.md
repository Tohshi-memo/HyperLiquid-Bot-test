# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T20:01:49.675970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0939` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.0429` n `230`; crypto_major avg `-0.0972` n `8`; equity avg `-0.0379` n `102`; fx avg `0.0039` n `6`; index avg `-0.0255` n `25`; metal avg `-0.0138` n `20`; unknown avg `-0.0255` n `782`
- 1h: commodity avg `0.0402` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `-0.1285` n `8`; equity avg `-0.031` n `102`; fx avg `0.0051` n `6`; index avg `-0.0302` n `25`; metal avg `0.0018` n `20`; unknown avg `0.0874` n `782`
- 4h: commodity avg `0.1022` n `12`; crypto_alt avg `-0.9883` n `230`; crypto_major avg `-1.1819` n `8`; equity avg `-0.3258` n `102`; fx avg `0.0063` n `6`; index avg `-0.088` n `25`; metal avg `0.0052` n `20`; unknown avg `2.9584` n `782`
- 24h: commodity avg `0.5679` n `12`; crypto_alt avg `-0.7194` n `230`; crypto_major avg `-1.2807` n `8`; equity avg `-0.8064` n `102`; fx avg `-0.1273` n `6`; index avg `-0.1266` n `25`; metal avg `-0.0202` n `20`; unknown avg `4.3409` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
