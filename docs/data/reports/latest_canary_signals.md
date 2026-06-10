# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T22:37:29.430774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0411` n `12`; crypto_alt avg `0.6095` n `228`; crypto_major avg `0.4095` n `8`; equity avg `0.0784` n `74`; fx avg `0.0177` n `6`; index avg `0.0459` n `23`; metal avg `0.5071` n `18`; unknown avg `0.1719` n `550`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.2744` n `228`; crypto_major avg `-0.2652` n `8`; equity avg `-0.3987` n `74`; fx avg `-0.0561` n `6`; index avg `-0.0951` n `23`; metal avg `-0.181` n `18`; unknown avg `0.3446` n `550`
- 4h: commodity avg `0.6304` n `12`; crypto_alt avg `-1.4776` n `228`; crypto_major avg `-0.9549` n `8`; equity avg `-1.5018` n `74`; fx avg `-0.0885` n `6`; index avg `-0.5565` n `23`; metal avg `-1.2213` n `18`; unknown avg `-0.0191` n `550`
- 24h: commodity avg `1.4078` n `12`; crypto_alt avg `-2.7502` n `228`; crypto_major avg `-2.7689` n `8`; equity avg `-2.238` n `74`; fx avg `-0.1022` n `6`; index avg `-1.674` n `23`; metal avg `-2.6518` n `18`; unknown avg `-0.4986` n `537`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
