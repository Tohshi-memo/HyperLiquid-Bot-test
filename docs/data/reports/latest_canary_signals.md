# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T14:52:31.604438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.4349` n `234`; crypto_major avg `-0.4265` n `8`; equity avg `0.0431` n `138`; fx avg `-0.0055` n `6`; index avg `-0.0303` n `26`; metal avg `-0.0573` n `20`; unknown avg `0.0506` n `919`
- 1h: commodity avg `0.0732` n `12`; crypto_alt avg `0.3397` n `234`; crypto_major avg `0.3184` n `8`; equity avg `-0.0976` n `138`; fx avg `-0.0298` n `6`; index avg `-0.035` n `26`; metal avg `-0.0447` n `20`; unknown avg `0.9019` n `903`
- 4h: commodity avg `0.0585` n `12`; crypto_alt avg `0.631` n `234`; crypto_major avg `1.0944` n `8`; equity avg `0.6229` n `138`; fx avg `-0.0872` n `6`; index avg `0.1444` n `26`; metal avg `0.2875` n `20`; unknown avg `1.0466` n `891`
- 24h: commodity avg `-0.3435` n `12`; crypto_alt avg `4.6048` n `234`; crypto_major avg `2.949` n `8`; equity avg `1.6959` n `138`; fx avg `0.0197` n `6`; index avg `0.2242` n `26`; metal avg `0.1524` n `20`; unknown avg `0.6142` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
