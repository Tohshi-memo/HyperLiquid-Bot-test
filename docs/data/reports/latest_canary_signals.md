# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T05:00:01.533827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1837` n `12`; crypto_alt avg `-0.0733` n `228`; crypto_major avg `0.0415` n `8`; equity avg `-0.0276` n `67`; fx avg `0.0011` n `6`; index avg `-0.0266` n `23`; metal avg `-0.0058` n `18`; unknown avg `-0.0101` n `386`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.3876` n `228`; crypto_major avg `-0.3152` n `8`; equity avg `-0.1102` n `67`; fx avg `0.0011` n `6`; index avg `-0.0621` n `23`; metal avg `-0.0306` n `18`; unknown avg `0.2362` n `386`
- 4h: commodity avg `0.0675` n `12`; crypto_alt avg `0.1514` n `228`; crypto_major avg `-0.0099` n `8`; equity avg `0.0152` n `67`; fx avg `-0.0014` n `6`; index avg `0.02` n `23`; metal avg `0.0174` n `18`; unknown avg `-1.1259` n `386`
- 24h: commodity avg `0.185` n `12`; crypto_alt avg `-3.9716` n `228`; crypto_major avg `-2.7635` n `8`; equity avg `-2.0681` n `67`; fx avg `0.0443` n `6`; index avg `-0.1484` n `23`; metal avg `-0.9747` n `18`; unknown avg `-2.0646` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
