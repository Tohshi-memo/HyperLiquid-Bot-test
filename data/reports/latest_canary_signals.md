# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T06:37:18.583686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.1031` n `228`; crypto_major avg `-0.0953` n `8`; equity avg `0.0569` n `67`; fx avg `0.001` n `6`; index avg `-0.0472` n `23`; metal avg `0.0062` n `18`; unknown avg `-0.249` n `386`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.0236` n `228`; crypto_major avg `-0.2005` n `8`; equity avg `0.0579` n `67`; fx avg `-0.0001` n `6`; index avg `-0.0567` n `23`; metal avg `0.0277` n `18`; unknown avg `-0.0763` n `376`
- 4h: commodity avg `0.1562` n `12`; crypto_alt avg `-0.3565` n `228`; crypto_major avg `-0.1844` n `8`; equity avg `-0.0021` n `67`; fx avg `0.0089` n `6`; index avg `-0.0808` n `23`; metal avg `0.0313` n `18`; unknown avg `-0.3236` n `376`
- 24h: commodity avg `-0.1604` n `12`; crypto_alt avg `-3.8543` n `228`; crypto_major avg `-2.6571` n `8`; equity avg `-1.9484` n `67`; fx avg `0.0542` n `6`; index avg `-0.1889` n `23`; metal avg `-0.7769` n `18`; unknown avg `-2.1192` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
