# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T09:28:24.564917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.0478` n `228`; crypto_major avg `0.179` n `8`; equity avg `0.0374` n `78`; fx avg `-0.0066` n `6`; index avg `0.0074` n `23`; metal avg `0.0116` n `18`; unknown avg `-0.0233` n `702`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `0.0983` n `228`; crypto_major avg `0.0489` n `8`; equity avg `-0.01` n `78`; fx avg `-0.002` n `6`; index avg `0.0074` n `23`; metal avg `0.001` n `18`; unknown avg `-0.033` n `702`
- 4h: commodity avg `-0.0563` n `12`; crypto_alt avg `0.3572` n `228`; crypto_major avg `-0.2835` n `8`; equity avg `0.0217` n `78`; fx avg `-0.0095` n `6`; index avg `0.0078` n `23`; metal avg `0.0303` n `18`; unknown avg `-0.1726` n `662`
- 24h: commodity avg `0.0796` n `12`; crypto_alt avg `1.0412` n `228`; crypto_major avg `-0.0312` n `8`; equity avg `0.2969` n `78`; fx avg `0.3257` n `6`; index avg `0.0264` n `23`; metal avg `-0.0178` n `18`; unknown avg `-0.0543` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
