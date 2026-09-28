# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T20:22:33.088100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0127` n `234`; crypto_major avg `0.0282` n `8`; equity avg `0.0066` n `141`; fx avg `-0.0024` n `6`; index avg `-0.011` n `26`; metal avg `0.0113` n `20`; unknown avg `-0.2609` n `921`
- 1h: commodity avg `-0.0909` n `12`; crypto_alt avg `0.0951` n `234`; crypto_major avg `-0.017` n `8`; equity avg `-0.2523` n `141`; fx avg `0.0065` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0869` n `20`; unknown avg `0.1489` n `899`
- 4h: commodity avg `0.0625` n `12`; crypto_alt avg `-0.3777` n `234`; crypto_major avg `-0.5607` n `8`; equity avg `-0.269` n `141`; fx avg `0.0138` n `6`; index avg `-0.0468` n `26`; metal avg `-0.1019` n `20`; unknown avg `4.7922` n `858`
- 24h: commodity avg `-0.331` n `12`; crypto_alt avg `-3.8039` n `234`; crypto_major avg `-2.0353` n `8`; equity avg `-3.4086` n `141`; fx avg `0.0413` n `6`; index avg `-0.3227` n `26`; metal avg `-1.1043` n `20`; unknown avg `26.3146` n `776`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
