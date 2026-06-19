# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T20:37:27.121833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `12`; crypto_alt avg `0.0219` n `228`; crypto_major avg `0.1148` n `8`; equity avg `-0.0013` n `78`; fx avg `-0.0412` n `6`; index avg `-0.004` n `23`; metal avg `0.0015` n `18`; unknown avg `0.0193` n `687`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `0.1404` n `228`; crypto_major avg `0.0098` n `8`; equity avg `0.0101` n `78`; fx avg `-0.0072` n `6`; index avg `-0.0094` n `23`; metal avg `0.0633` n `18`; unknown avg `-0.1427` n `687`
- 4h: commodity avg `-0.0734` n `12`; crypto_alt avg `-0.7407` n `228`; crypto_major avg `-0.3467` n `8`; equity avg `-0.1733` n `78`; fx avg `-0.0211` n `6`; index avg `-0.0534` n `23`; metal avg `0.2553` n `18`; unknown avg `-0.0513` n `687`
- 24h: commodity avg `0.3011` n `12`; crypto_alt avg `-3.8991` n `228`; crypto_major avg `-4.7227` n `8`; equity avg `0.6623` n `78`; fx avg `-0.1433` n `6`; index avg `0.2199` n `23`; metal avg `-4.1599` n `18`; unknown avg `-0.3936` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
