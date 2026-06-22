# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T03:37:31.929575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0434` n `228`; crypto_major avg `-0.1224` n `8`; equity avg `0.0653` n `79`; fx avg `0.0011` n `6`; index avg `-0.0135` n `23`; metal avg `-0.0107` n `18`; unknown avg `1.3437` n `701`
- 1h: commodity avg `0.0928` n `12`; crypto_alt avg `-0.4073` n `228`; crypto_major avg `-0.6098` n `8`; equity avg `0.024` n `79`; fx avg `-0.0119` n `6`; index avg `0.0183` n `23`; metal avg `-0.1916` n `18`; unknown avg `2.499` n `701`
- 4h: commodity avg `-0.4113` n `12`; crypto_alt avg `1.4448` n `228`; crypto_major avg `1.1303` n `8`; equity avg `0.3643` n `79`; fx avg `0.1453` n `6`; index avg `0.1882` n `23`; metal avg `0.3617` n `18`; unknown avg `2.1399` n `685`
- 24h: commodity avg `-0.2691` n `12`; crypto_alt avg `0.162` n `228`; crypto_major avg `-0.7425` n `8`; equity avg `-0.3481` n `79`; fx avg `0.0226` n `6`; index avg `0.015` n `23`; metal avg `0.1002` n `18`; unknown avg `0.2296` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
