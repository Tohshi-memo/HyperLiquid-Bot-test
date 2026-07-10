# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T02:07:30.638107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.2567` n `229`; crypto_major avg `-0.2942` n `8`; equity avg `-0.159` n `91`; fx avg `-0.0318` n `6`; index avg `-0.0398` n `25`; metal avg `0.033` n `20`; unknown avg `0.2613` n `763`
- 1h: commodity avg `0.056` n `12`; crypto_alt avg `0.7978` n `229`; crypto_major avg `0.9343` n `8`; equity avg `0.1709` n `91`; fx avg `0.0091` n `6`; index avg `0.0456` n `25`; metal avg `0.0222` n `20`; unknown avg `0.9435` n `763`
- 4h: commodity avg `0.0843` n `12`; crypto_alt avg `0.7106` n `229`; crypto_major avg `0.8215` n `8`; equity avg `0.0571` n `91`; fx avg `0.001` n `6`; index avg `-0.0439` n `25`; metal avg `0.086` n `20`; unknown avg `0.1394` n `763`
- 24h: commodity avg `-0.9924` n `12`; crypto_alt avg `1.5036` n `229`; crypto_major avg `1.4546` n `8`; equity avg `1.3429` n `91`; fx avg `0.0228` n `6`; index avg `0.3731` n `25`; metal avg `0.6879` n `20`; unknown avg `-0.0238` n `746`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
