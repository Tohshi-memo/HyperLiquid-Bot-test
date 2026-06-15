# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T04:07:29.291929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0814` n `12`; crypto_alt avg `0.0092` n `228`; crypto_major avg `-0.028` n `8`; equity avg `-0.0579` n `74`; fx avg `0.0034` n `6`; index avg `-0.0872` n `23`; metal avg `-0.042` n `18`; unknown avg `0.0594` n `645`
- 1h: commodity avg `0.1503` n `12`; crypto_alt avg `0.235` n `228`; crypto_major avg `0.2553` n `8`; equity avg `0.0689` n `74`; fx avg `0.0123` n `6`; index avg `0.0712` n `23`; metal avg `-0.0737` n `18`; unknown avg `-0.5711` n `637`
- 4h: commodity avg `-0.113` n `12`; crypto_alt avg `0.4196` n `228`; crypto_major avg `0.2443` n `8`; equity avg `0.3241` n `74`; fx avg `0.0725` n `6`; index avg `0.2788` n `23`; metal avg `0.2954` n `18`; unknown avg `-0.4103` n `629`
- 24h: commodity avg `-0.9217` n `12`; crypto_alt avg `2.4495` n `228`; crypto_major avg `2.5787` n `8`; equity avg `1.7583` n `74`; fx avg `0.0178` n `6`; index avg `0.8252` n `23`; metal avg `1.9918` n `18`; unknown avg `3.2994` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
