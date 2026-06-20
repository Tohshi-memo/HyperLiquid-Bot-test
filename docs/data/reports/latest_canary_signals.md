# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T04:37:25.963950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0637` n `228`; crypto_major avg `0.1889` n `8`; equity avg `0.0155` n `78`; fx avg `-0.0132` n `6`; index avg `0.0167` n `23`; metal avg `0.0082` n `18`; unknown avg `-0.0769` n `687`
- 1h: commodity avg `-0.0401` n `12`; crypto_alt avg `0.1841` n `228`; crypto_major avg `0.2864` n `8`; equity avg `0.1254` n `78`; fx avg `-0.0258` n `6`; index avg `0.0142` n `23`; metal avg `0.0456` n `18`; unknown avg `0.9795` n `687`
- 4h: commodity avg `0.1357` n `12`; crypto_alt avg `-0.6626` n `228`; crypto_major avg `-0.0808` n `8`; equity avg `0.1023` n `78`; fx avg `-0.0226` n `6`; index avg `0.0273` n `23`; metal avg `-0.0311` n `18`; unknown avg `-0.4963` n `679`
- 24h: commodity avg `0.4163` n `12`; crypto_alt avg `-3.5667` n `228`; crypto_major avg `-4.1962` n `8`; equity avg `1.1132` n `78`; fx avg `-0.1011` n `6`; index avg `0.3127` n `23`; metal avg `-4.1211` n `18`; unknown avg `-0.3956` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
