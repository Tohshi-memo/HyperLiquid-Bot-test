# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T15:39:24.352324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2273` n `12`; crypto_alt avg `0.119` n `228`; crypto_major avg `-0.0331` n `8`; equity avg `-0.0055` n `67`; fx avg `-0.0055` n `6`; index avg `0.0526` n `23`; metal avg `0.0741` n `18`; unknown avg `1.0279` n `386`
- 1h: commodity avg `-0.3215` n `12`; crypto_alt avg `-0.2318` n `228`; crypto_major avg `-0.3042` n `8`; equity avg `0.0229` n `67`; fx avg `0.0221` n `6`; index avg `0.1262` n `23`; metal avg `0.4364` n `18`; unknown avg `0.9416` n `386`
- 4h: commodity avg `-1.0121` n `12`; crypto_alt avg `-0.6091` n `228`; crypto_major avg `-0.369` n `8`; equity avg `0.0928` n `67`; fx avg `-0.0037` n `6`; index avg `0.4616` n `23`; metal avg `-0.3676` n `18`; unknown avg `1.9234` n `386`
- 24h: commodity avg `-2.2492` n `12`; crypto_alt avg `0.958` n `228`; crypto_major avg `-0.3931` n `8`; equity avg `0.9921` n `67`; fx avg `0.1528` n `6`; index avg `1.3241` n `23`; metal avg `0.133` n `18`; unknown avg `0.6164` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0414`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0397`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0339`, n `668`, weak_sample_signal
