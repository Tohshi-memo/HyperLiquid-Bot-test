# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T16:41:34.531081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0961` n `230`; crypto_major avg `-0.0003` n `8`; equity avg `-0.0655` n `113`; fx avg `-0.0008` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0718` n `20`; unknown avg `-0.0637` n `786`
- 1h: commodity avg `-0.0589` n `12`; crypto_alt avg `-0.0695` n `230`; crypto_major avg `-0.0948` n `8`; equity avg `0.2587` n `113`; fx avg `-0.0137` n `6`; index avg `0.0158` n `25`; metal avg `-0.0608` n `20`; unknown avg `-0.0268` n `786`
- 4h: commodity avg `-0.1282` n `12`; crypto_alt avg `-0.8082` n `230`; crypto_major avg `-0.706` n `8`; equity avg `0.6263` n `113`; fx avg `-0.0098` n `6`; index avg `0.0541` n `25`; metal avg `-0.2608` n `20`; unknown avg `0.1054` n `786`
- 24h: commodity avg `0.1257` n `12`; crypto_alt avg `-0.1927` n `230`; crypto_major avg `1.003` n `8`; equity avg `3.5491` n `113`; fx avg `0.0448` n `6`; index avg `0.3479` n `25`; metal avg `0.1921` n `20`; unknown avg `0.0053` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2031`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
