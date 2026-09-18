# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T19:22:27.976395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.236` n `234`; crypto_major avg `0.3561` n `8`; equity avg `0.1497` n `140`; fx avg `0.0032` n `6`; index avg `0.0053` n `26`; metal avg `0.0097` n `20`; unknown avg `1.1853` n `940`
- 1h: commodity avg `-0.079` n `12`; crypto_alt avg `0.5427` n `234`; crypto_major avg `0.5202` n `8`; equity avg `0.2803` n `140`; fx avg `-0.0015` n `6`; index avg `0.0496` n `26`; metal avg `-0.0818` n `20`; unknown avg `6.694` n `938`
- 4h: commodity avg `-0.2957` n `12`; crypto_alt avg `1.1264` n `234`; crypto_major avg `0.8832` n `8`; equity avg `0.6457` n `140`; fx avg `-0.0085` n `6`; index avg `0.091` n `26`; metal avg `0.1157` n `20`; unknown avg `3.7739` n `908`
- 24h: commodity avg `-0.1059` n `12`; crypto_alt avg `6.8821` n `234`; crypto_major avg `7.3414` n `8`; equity avg `1.0584` n `140`; fx avg `0.1972` n `6`; index avg `-0.0383` n `26`; metal avg `0.3828` n `20`; unknown avg `6.2825` n `717`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
