# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T08:37:13.344863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.0089` n `228`; crypto_major avg `0.0712` n `8`; equity avg `0.0045` n `65`; fx avg `0.0017` n `5`; index avg `-0.0181` n `23`; metal avg `0.0029` n `18`; unknown avg `0.053` n `376`
- 1h: commodity avg `-0.1051` n `12`; crypto_alt avg `0.161` n `228`; crypto_major avg `0.1127` n `8`; equity avg `-0.0197` n `65`; fx avg `0.0045` n `5`; index avg `-0.0207` n `23`; metal avg `0.0038` n `18`; unknown avg `0.1879` n `376`
- 4h: commodity avg `-0.0914` n `12`; crypto_alt avg `0.5505` n `228`; crypto_major avg `0.2274` n `8`; equity avg `0.0183` n `65`; fx avg `0.0064` n `5`; index avg `-0.0217` n `23`; metal avg `-0.0082` n `18`; unknown avg `-0.0478` n `366`
- 24h: commodity avg `0.0726` n `12`; crypto_alt avg `-0.7652` n `228`; crypto_major avg `-0.3381` n `8`; equity avg `0.852` n `65`; fx avg `-0.0201` n `5`; index avg `0.2152` n `23`; metal avg `0.3389` n `18`; unknown avg `-0.0566` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
