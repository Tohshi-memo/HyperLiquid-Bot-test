# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T16:24:08.338225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.458` n `12`; crypto_alt avg `0.8727` n `228`; crypto_major avg `0.8012` n `8`; equity avg `0.2303` n `67`; fx avg `0.0018` n `6`; index avg `0.1882` n `23`; metal avg `0.4778` n `18`; unknown avg `0.4989` n `419`
- 1h: commodity avg `-0.3091` n `12`; crypto_alt avg `1.1311` n `228`; crypto_major avg `1.0068` n `8`; equity avg `0.3269` n `67`; fx avg `0.0039` n `6`; index avg `0.2314` n `23`; metal avg `0.7632` n `18`; unknown avg `0.2202` n `419`
- 4h: commodity avg `-0.0923` n `12`; crypto_alt avg `1.1643` n `228`; crypto_major avg `1.416` n `8`; equity avg `2.2348` n `67`; fx avg `0.0348` n `6`; index avg `1.3734` n `23`; metal avg `2.3238` n `18`; unknown avg `0.3502` n `419`
- 24h: commodity avg `0.2827` n `12`; crypto_alt avg `-4.8411` n `228`; crypto_major avg `-2.1588` n `8`; equity avg `1.4118` n `67`; fx avg `0.0087` n `6`; index avg `1.0067` n `23`; metal avg `0.6993` n `18`; unknown avg `-0.9349` n `408`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
