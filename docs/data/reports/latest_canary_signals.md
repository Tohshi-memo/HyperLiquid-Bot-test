# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T22:22:31.092376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `0.0204` n `230`; crypto_major avg `-0.0329` n `8`; equity avg `0.002` n `112`; fx avg `-0.0016` n `6`; index avg `0.0032` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0225` n `784`
- 1h: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `-0.2042` n `8`; equity avg `0.013` n `112`; fx avg `-0.0003` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0178` n `784`
- 4h: commodity avg `0.058` n `12`; crypto_alt avg `0.0368` n `230`; crypto_major avg `-0.1855` n `8`; equity avg `0.1217` n `112`; fx avg `0.0017` n `6`; index avg `0.0077` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.2571` n `784`
- 24h: commodity avg `0.2218` n `12`; crypto_alt avg `1.8587` n `230`; crypto_major avg `1.2543` n `8`; equity avg `0.652` n `112`; fx avg `-0.0076` n `6`; index avg `0.0269` n `25`; metal avg `0.0277` n `20`; unknown avg `0.2049` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
