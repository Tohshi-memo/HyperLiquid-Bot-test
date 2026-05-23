# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T05:52:12.351017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `0.1282` n `228`; crypto_major avg `-0.0012` n `8`; equity avg `-0.0098` n `67`; fx avg `0.0` n `6`; index avg `-0.0228` n `23`; metal avg `-0.002` n `18`; unknown avg `-0.2597` n `386`
- 1h: commodity avg `0.1228` n `12`; crypto_alt avg `-0.1481` n `228`; crypto_major avg `0.0119` n `8`; equity avg `-0.0429` n `67`; fx avg `0.0098` n `6`; index avg `-0.0715` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.0537` n `386`
- 4h: commodity avg `-0.0746` n `12`; crypto_alt avg `-0.1` n `228`; crypto_major avg `0.029` n `8`; equity avg `-0.1213` n `67`; fx avg `0.0066` n `6`; index avg `-0.0484` n `23`; metal avg `-0.008` n `18`; unknown avg `-0.8954` n `386`
- 24h: commodity avg `-0.0535` n `12`; crypto_alt avg `-4.2393` n `228`; crypto_major avg `-2.7862` n `8`; equity avg `-2.0978` n `67`; fx avg `0.0331` n `6`; index avg `-0.2855` n `23`; metal avg `-1.1558` n `18`; unknown avg `-2.5281` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
