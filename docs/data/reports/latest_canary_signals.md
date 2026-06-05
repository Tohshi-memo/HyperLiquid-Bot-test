# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T14:22:28.127694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1137` n `12`; crypto_alt avg `0.5741` n `228`; crypto_major avg `0.3535` n `8`; equity avg `0.235` n `74`; fx avg `-0.009` n `6`; index avg `-0.0447` n `23`; metal avg `-0.3462` n `18`; unknown avg `0.48` n `424`
- 1h: commodity avg `-0.2095` n `12`; crypto_alt avg `-1.1466` n `228`; crypto_major avg `-1.6789` n `8`; equity avg `-1.5161` n `74`; fx avg `-0.0776` n `6`; index avg `-1.0693` n `23`; metal avg `-1.5896` n `18`; unknown avg `-0.2061` n `424`
- 4h: commodity avg `-0.5987` n `12`; crypto_alt avg `-1.2838` n `228`; crypto_major avg `-1.5329` n `8`; equity avg `-2.4117` n `74`; fx avg `-0.0845` n `6`; index avg `-1.4478` n `23`; metal avg `-2.5202` n `18`; unknown avg `1.9968` n `424`
- 24h: commodity avg `-0.6689` n `12`; crypto_alt avg `-6.7272` n `228`; crypto_major avg `-5.5126` n `8`; equity avg `-3.3447` n `74`; fx avg `0.0175` n `6`; index avg `-1.6004` n `23`; metal avg `-3.0948` n `18`; unknown avg `-0.1709` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
