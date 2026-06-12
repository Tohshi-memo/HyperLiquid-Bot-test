# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T01:37:41.359125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `-0.1267` n `228`; crypto_major avg `-0.2561` n `8`; equity avg `-0.1478` n `74`; fx avg `0.0283` n `6`; index avg `-0.1787` n `23`; metal avg `-0.1574` n `18`; unknown avg `0.2194` n `556`
- 1h: commodity avg `-0.0466` n `12`; crypto_alt avg `-0.7435` n `228`; crypto_major avg `-0.7481` n `8`; equity avg `-0.6475` n `74`; fx avg `0.0152` n `6`; index avg `-0.2777` n `23`; metal avg `-0.719` n `18`; unknown avg `0.082` n `556`
- 4h: commodity avg `0.0879` n `12`; crypto_alt avg `-0.6726` n `228`; crypto_major avg `-0.5258` n `8`; equity avg `0.2906` n `74`; fx avg `0.0063` n `6`; index avg `-0.0135` n `23`; metal avg `-0.3934` n `18`; unknown avg `6.2186` n `556`
- 24h: commodity avg `-2.2632` n `12`; crypto_alt avg `2.5797` n `228`; crypto_major avg `2.689` n `8`; equity avg `3.4232` n `74`; fx avg `-0.0322` n `6`; index avg `1.8514` n `23`; metal avg `1.9375` n `18`; unknown avg `2.6126` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
