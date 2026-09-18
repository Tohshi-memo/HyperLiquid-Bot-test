# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T06:52:25.694375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `0.0836` n `234`; crypto_major avg `-0.0095` n `8`; equity avg `0.0038` n `140`; fx avg `-0.0279` n `6`; index avg `0.0014` n `26`; metal avg `0.0096` n `20`; unknown avg `-0.0679` n `927`
- 1h: commodity avg `-0.1677` n `12`; crypto_alt avg `0.3537` n `234`; crypto_major avg `0.1466` n `8`; equity avg `0.3079` n `140`; fx avg `0.001` n `6`; index avg `0.056` n `26`; metal avg `0.1109` n `20`; unknown avg `0.0435` n `871`
- 4h: commodity avg `-0.2096` n `12`; crypto_alt avg `1.2112` n `234`; crypto_major avg `1.1974` n `8`; equity avg `0.9297` n `140`; fx avg `0.1002` n `6`; index avg `0.1638` n `26`; metal avg `0.2707` n `20`; unknown avg `0.0483` n `863`
- 24h: commodity avg `-0.2663` n `12`; crypto_alt avg `4.9766` n `234`; crypto_major avg `3.6131` n `8`; equity avg `2.4134` n `140`; fx avg `0.1226` n `6`; index avg `0.347` n `26`; metal avg `0.6601` n `20`; unknown avg `2.5224` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
