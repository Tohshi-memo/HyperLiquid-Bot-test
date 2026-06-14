# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T18:07:29.642069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.0139` n `228`; crypto_major avg `-0.0454` n `8`; equity avg `-0.0137` n `74`; fx avg `0.0146` n `6`; index avg `-0.0189` n `23`; metal avg `0.148` n `18`; unknown avg `-0.2288` n `645`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `-0.4665` n `228`; crypto_major avg `-0.2421` n `8`; equity avg `-0.0547` n `74`; fx avg `-0.0069` n `6`; index avg `-0.0094` n `23`; metal avg `-0.0057` n `18`; unknown avg `-0.4087` n `645`
- 4h: commodity avg `-0.1986` n `12`; crypto_alt avg `-0.6303` n `228`; crypto_major avg `-0.6049` n `8`; equity avg `-0.1398` n `74`; fx avg `-0.0241` n `6`; index avg `0.0515` n `23`; metal avg `-0.0145` n `18`; unknown avg `-0.2796` n `645`
- 24h: commodity avg `-0.0017` n `12`; crypto_alt avg `-1.5815` n `228`; crypto_major avg `-0.5667` n `8`; equity avg `0.3654` n `74`; fx avg `-0.0207` n `6`; index avg `0.2689` n `23`; metal avg `-0.1401` n `18`; unknown avg `1.1017` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
