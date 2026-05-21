# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T12:22:20.369222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.93` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1202` n `12`; crypto_alt avg `0.0194` n `228`; crypto_major avg `0.0083` n `8`; equity avg `-0.0896` n `66`; fx avg `-0.0125` n `6`; index avg `-0.0639` n `23`; metal avg `-0.3331` n `18`; unknown avg `-0.004` n `386`
- 1h: commodity avg `0.1838` n `12`; crypto_alt avg `-0.2431` n `228`; crypto_major avg `-0.1608` n `8`; equity avg `-0.1422` n `66`; fx avg `-0.0497` n `6`; index avg `-0.1256` n `23`; metal avg `-0.3961` n `18`; unknown avg `-0.1786` n `386`
- 4h: commodity avg `0.7314` n `12`; crypto_alt avg `-1.1165` n `228`; crypto_major avg `-1.2678` n `8`; equity avg `-0.4941` n `66`; fx avg `-0.0252` n `6`; index avg `-0.4193` n `23`; metal avg `-0.6757` n `18`; unknown avg `1.3661` n `386`
- 24h: commodity avg `-0.9135` n `12`; crypto_alt avg `1.7439` n `228`; crypto_major avg `2.1298` n `8`; equity avg `0.9606` n `66`; fx avg `0.031` n `6`; index avg `0.8018` n `23`; metal avg `-0.337` n `18`; unknown avg `6.5439` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
