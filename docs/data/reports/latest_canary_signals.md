# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T18:07:17.228275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2555` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1752` n `12`; crypto_alt avg `-0.4065` n `228`; crypto_major avg `-0.1016` n `8`; equity avg `-0.048` n `67`; fx avg `-0.0001` n `6`; index avg `0.0108` n `23`; metal avg `-0.0687` n `18`; unknown avg `-0.1762` n `386`
- 1h: commodity avg `0.0715` n `12`; crypto_alt avg `-0.5242` n `228`; crypto_major avg `-0.2244` n `8`; equity avg `-0.1645` n `67`; fx avg `-0.0045` n `6`; index avg `-0.0002` n `23`; metal avg `-0.0861` n `18`; unknown avg `0.1371` n `386`
- 4h: commodity avg `-0.8162` n `12`; crypto_alt avg `-0.9567` n `228`; crypto_major avg `-0.9358` n `8`; equity avg `-0.0323` n `67`; fx avg `0.0622` n `6`; index avg `0.3197` n `23`; metal avg `0.222` n `18`; unknown avg `-0.5402` n `386`
- 24h: commodity avg `-0.7551` n `12`; crypto_alt avg `-0.6001` n `228`; crypto_major avg `-0.9041` n `8`; equity avg `-0.2884` n `67`; fx avg `0.184` n `6`; index avg `0.72` n `23`; metal avg `-0.8069` n `18`; unknown avg `-0.463` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0418`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0406`, n `668`, weak_sample_signal
