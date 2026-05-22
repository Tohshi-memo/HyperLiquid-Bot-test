# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T17:30:10.620271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2208` n `12`; crypto_alt avg `0.4015` n `228`; crypto_major avg `0.2459` n `8`; equity avg `0.2821` n `67`; fx avg `-0.0022` n `6`; index avg `0.0531` n `23`; metal avg `0.202` n `18`; unknown avg `0.0092` n `386`
- 1h: commodity avg `-0.1164` n `12`; crypto_alt avg `0.479` n `228`; crypto_major avg `0.2093` n `8`; equity avg `0.2248` n `67`; fx avg `0.0009` n `6`; index avg `0.0654` n `23`; metal avg `0.1277` n `18`; unknown avg `-0.163` n `386`
- 4h: commodity avg `-0.497` n `12`; crypto_alt avg `-0.8289` n `228`; crypto_major avg `-0.8568` n `8`; equity avg `-0.4056` n `67`; fx avg `0.0571` n `6`; index avg `0.1432` n `23`; metal avg `0.0557` n `18`; unknown avg `-0.9159` n `386`
- 24h: commodity avg `-1.2428` n `12`; crypto_alt avg `0.131` n `228`; crypto_major avg `-0.9135` n `8`; equity avg `0.2271` n `67`; fx avg `0.1818` n `6`; index avg `0.8428` n `23`; metal avg `-0.6356` n `18`; unknown avg `-1.4445` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0396`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0395`, n `668`, weak_sample_signal
