# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T04:07:19.496836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `12`; crypto_alt avg `-0.2005` n `228`; crypto_major avg `-0.0866` n `8`; equity avg `0.0221` n `67`; fx avg `-0.0012` n `6`; index avg `0.0018` n `23`; metal avg `-0.0047` n `18`; unknown avg `-0.3759` n `386`
- 1h: commodity avg `0.214` n `12`; crypto_alt avg `-0.0012` n `228`; crypto_major avg `0.1363` n `8`; equity avg `-0.0366` n `67`; fx avg `-0.0034` n `6`; index avg `0.0032` n `23`; metal avg `-0.0096` n `18`; unknown avg `-0.3746` n `386`
- 4h: commodity avg `0.2615` n `12`; crypto_alt avg `0.8036` n `228`; crypto_major avg `0.3264` n `8`; equity avg `-0.0395` n `67`; fx avg `-0.0045` n `6`; index avg `-0.0139` n `23`; metal avg `-0.0036` n `18`; unknown avg `-0.9395` n `386`
- 24h: commodity avg `0.2516` n `12`; crypto_alt avg `-3.751` n `228`; crypto_major avg `-2.5356` n `8`; equity avg `-1.8825` n `67`; fx avg `0.0614` n `6`; index avg `-0.0585` n `23`; metal avg `-0.9155` n `18`; unknown avg `-2.0131` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
