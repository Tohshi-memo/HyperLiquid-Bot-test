# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T04:22:32.865073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.99` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0476` n `12`; crypto_alt avg `0.178` n `228`; crypto_major avg `0.046` n `8`; equity avg `0.034` n `74`; fx avg `0.0061` n `6`; index avg `0.024` n `23`; metal avg `-0.0241` n `18`; unknown avg `-0.0198` n `645`
- 1h: commodity avg `0.1326` n `12`; crypto_alt avg `0.2554` n `228`; crypto_major avg `0.2089` n `8`; equity avg `-0.0263` n `74`; fx avg `0.023` n `6`; index avg `0.0918` n `23`; metal avg `-0.1081` n `18`; unknown avg `-0.5753` n `637`
- 4h: commodity avg `-0.0669` n `12`; crypto_alt avg `0.556` n `228`; crypto_major avg `0.171` n `8`; equity avg `0.1752` n `74`; fx avg `0.0716` n `6`; index avg `0.1437` n `23`; metal avg `0.0747` n `18`; unknown avg `-0.3959` n `629`
- 24h: commodity avg `-0.9681` n `12`; crypto_alt avg `2.622` n `228`; crypto_major avg `2.671` n `8`; equity avg `1.8076` n `74`; fx avg `0.0337` n `6`; index avg `0.8466` n `23`; metal avg `1.961` n `18`; unknown avg `3.2795` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
