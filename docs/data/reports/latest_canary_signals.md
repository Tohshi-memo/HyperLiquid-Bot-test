# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T16:52:20.910237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0879` n `12`; crypto_alt avg `-0.0708` n `228`; crypto_major avg `-0.1019` n `8`; equity avg `-0.0424` n `67`; fx avg `-0.0023` n `6`; index avg `-0.0226` n `23`; metal avg `-0.0295` n `18`; unknown avg `0.4223` n `385`
- 1h: commodity avg `-0.4951` n `12`; crypto_alt avg `-0.3162` n `228`; crypto_major avg `-0.6433` n `8`; equity avg `0.0667` n `67`; fx avg `0.016` n `6`; index avg `0.0276` n `23`; metal avg `0.188` n `18`; unknown avg `0.1475` n `385`
- 4h: commodity avg `-0.2481` n `12`; crypto_alt avg `0.5122` n `228`; crypto_major avg `0.2817` n `8`; equity avg `0.5452` n `67`; fx avg `-0.0442` n `6`; index avg `0.09` n `23`; metal avg `0.7412` n `18`; unknown avg `1.4348` n `385`
- 24h: commodity avg `0.6833` n `12`; crypto_alt avg `0.9315` n `228`; crypto_major avg `1.6084` n `8`; equity avg `0.9818` n `66`; fx avg `0.0066` n `6`; index avg `0.1916` n `23`; metal avg `-0.0515` n `18`; unknown avg `7.1389` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
