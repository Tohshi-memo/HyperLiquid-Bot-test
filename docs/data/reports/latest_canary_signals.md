# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T10:22:30.599226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0943` n `12`; crypto_alt avg `0.1246` n `230`; crypto_major avg `0.0758` n `8`; equity avg `-0.0287` n `108`; fx avg `-0.0009` n `6`; index avg `-0.0041` n `25`; metal avg `-0.008` n `20`; unknown avg `-0.0159` n `782`
- 1h: commodity avg `0.0852` n `12`; crypto_alt avg `-0.0878` n `230`; crypto_major avg `-0.29` n `8`; equity avg `0.1744` n `108`; fx avg `-0.0092` n `6`; index avg `0.0293` n `25`; metal avg `-0.0472` n `20`; unknown avg `91.6935` n `782`
- 4h: commodity avg `0.0242` n `12`; crypto_alt avg `-0.2027` n `230`; crypto_major avg `-0.5134` n `8`; equity avg `0.0218` n `108`; fx avg `0.0112` n `6`; index avg `0.0035` n `25`; metal avg `0.1591` n `20`; unknown avg `91.7387` n `782`
- 24h: commodity avg `-0.2278` n `12`; crypto_alt avg `0.0395` n `230`; crypto_major avg `-0.4519` n `8`; equity avg `-1.468` n `108`; fx avg `-0.0315` n `6`; index avg `-0.2957` n `25`; metal avg `0.5247` n `20`; unknown avg `95.8458` n `750`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
