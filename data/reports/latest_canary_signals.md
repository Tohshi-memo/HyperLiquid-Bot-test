# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T10:52:30.841029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `0.0578` n `230`; crypto_major avg `0.0131` n `8`; equity avg `-0.0157` n `112`; fx avg `-0.0111` n `6`; index avg `0.0123` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0672` n `784`
- 1h: commodity avg `0.0465` n `12`; crypto_alt avg `0.1065` n `230`; crypto_major avg `0.1085` n `8`; equity avg `0.0462` n `112`; fx avg `-0.0226` n `6`; index avg `0.0039` n `25`; metal avg `-0.0034` n `20`; unknown avg `1.1507` n `784`
- 4h: commodity avg `0.0703` n `12`; crypto_alt avg `0.2614` n `230`; crypto_major avg `0.197` n `8`; equity avg `0.1972` n `112`; fx avg `-0.0204` n `6`; index avg `0.0197` n `25`; metal avg `0.0453` n `20`; unknown avg `1.2524` n `784`
- 24h: commodity avg `0.1817` n `12`; crypto_alt avg `0.2292` n `230`; crypto_major avg `0.1758` n `8`; equity avg `0.9001` n `112`; fx avg `-0.0313` n `6`; index avg `0.053` n `25`; metal avg `-0.0442` n `20`; unknown avg `1.0856` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
