# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T13:52:19.699406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.1099` n `228`; crypto_major avg `0.1012` n `8`; equity avg `-0.0055` n `67`; fx avg `0.0005` n `6`; index avg `0.0124` n `23`; metal avg `0.0007` n `18`; unknown avg `-0.0948` n `396`
- 1h: commodity avg `-0.0839` n `12`; crypto_alt avg `0.896` n `228`; crypto_major avg `0.5393` n `8`; equity avg `0.1872` n `67`; fx avg `-0.0001` n `6`; index avg `0.0886` n `23`; metal avg `0.0426` n `18`; unknown avg `-0.1898` n `396`
- 4h: commodity avg `-0.0478` n `12`; crypto_alt avg `0.8862` n `228`; crypto_major avg `0.5326` n `8`; equity avg `0.2256` n `67`; fx avg `-0.0` n `6`; index avg `0.2154` n `23`; metal avg `0.0034` n `18`; unknown avg `-0.3635` n `396`
- 24h: commodity avg `0.048` n `12`; crypto_alt avg `-5.0982` n `228`; crypto_major avg `-4.0259` n `8`; equity avg `-1.7951` n `67`; fx avg `0.0624` n `6`; index avg `-0.341` n `23`; metal avg `-0.3687` n `18`; unknown avg `-3.1781` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
