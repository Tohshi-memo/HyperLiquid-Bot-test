# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T09:32:16.647154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.5616` n `12`; crypto_alt avg `0.0239` n `228`; crypto_major avg `-0.1094` n `8`; equity avg `0.0546` n `74`; fx avg `-0.0246` n `6`; index avg `-0.0866` n `23`; metal avg `0.542` n `18`; unknown avg `0.0739` n `635`
- 1h: commodity avg `0.2517` n `12`; crypto_alt avg `0.1191` n `228`; crypto_major avg `-0.1637` n `8`; equity avg `0.0939` n `74`; fx avg `-0.0362` n `6`; index avg `-0.0251` n `23`; metal avg `0.7616` n `18`; unknown avg `0.4314` n `635`
- 4h: commodity avg `0.1596` n `12`; crypto_alt avg `1.4682` n `228`; crypto_major avg `0.8295` n `8`; equity avg `0.3317` n `74`; fx avg `-0.0682` n `6`; index avg `-0.0403` n `23`; metal avg `0.8779` n `18`; unknown avg `0.585` n `619`
- 24h: commodity avg `0.5722` n `12`; crypto_alt avg `0.5889` n `228`; crypto_major avg `-0.2845` n `8`; equity avg `-0.76` n `74`; fx avg `-0.0144` n `6`; index avg `0.4737` n `23`; metal avg `0.7782` n `18`; unknown avg `31.3434` n `611`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
