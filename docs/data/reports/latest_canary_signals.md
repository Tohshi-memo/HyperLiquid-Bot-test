# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T17:07:20.639895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5349` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1957` n `12`; crypto_alt avg `0.0891` n `228`; crypto_major avg `0.0633` n `8`; equity avg `0.1095` n `67`; fx avg `0.0031` n `6`; index avg `0.0992` n `23`; metal avg `0.1867` n `18`; unknown avg `-0.0154` n `386`
- 1h: commodity avg `-0.3223` n `12`; crypto_alt avg `0.0827` n `228`; crypto_major avg `0.1716` n `8`; equity avg `0.0258` n `67`; fx avg `0.0258` n `6`; index avg `0.1164` n `23`; metal avg `0.0679` n `18`; unknown avg `-0.2154` n `386`
- 4h: commodity avg `-0.4976` n `12`; crypto_alt avg `-1.3897` n `228`; crypto_major avg `-1.1419` n `8`; equity avg `-0.1654` n `67`; fx avg `0.0677` n `6`; index avg `0.393` n `23`; metal avg `-0.1312` n `18`; unknown avg `-0.6586` n `386`
- 24h: commodity avg `-2.0653` n `12`; crypto_alt avg `1.1129` n `228`; crypto_major avg `-0.0226` n `8`; equity avg `0.7289` n `67`; fx avg `0.1865` n `6`; index avg `1.3159` n `23`; metal avg `-0.0949` n `18`; unknown avg `-0.8074` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0406`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0398`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0396`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0389`, n `668`, weak_sample_signal
