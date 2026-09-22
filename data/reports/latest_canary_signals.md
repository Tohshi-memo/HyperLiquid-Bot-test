# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T16:07:32.585417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0347` n `12`; crypto_alt avg `-0.0957` n `234`; crypto_major avg `-0.116` n `8`; equity avg `0.0746` n `140`; fx avg `0.0069` n `6`; index avg `0.0238` n `26`; metal avg `0.0039` n `20`; unknown avg `-0.1966` n `928`
- 1h: commodity avg `0.0829` n `12`; crypto_alt avg `0.2804` n `234`; crypto_major avg `0.0138` n `8`; equity avg `0.1177` n `140`; fx avg `0.0133` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0784` n `20`; unknown avg `0.7146` n `920`
- 4h: commodity avg `0.5436` n `12`; crypto_alt avg `1.0583` n `234`; crypto_major avg `0.5458` n `8`; equity avg `0.7668` n `140`; fx avg `-0.0056` n `6`; index avg `0.088` n `26`; metal avg `0.0177` n `20`; unknown avg `2.6671` n `886`
- 24h: commodity avg `0.2876` n `12`; crypto_alt avg `1.0015` n `234`; crypto_major avg `1.1053` n `8`; equity avg `0.7157` n `140`; fx avg `-0.2832` n `6`; index avg `0.1157` n `26`; metal avg `-0.1115` n `20`; unknown avg `3978.0319` n `834`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
