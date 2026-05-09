# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T05:22:11.359015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `0.1195` n `228`; crypto_major avg `0.1837` n `8`; equity avg `0.0155` n `65`; fx avg `0.0` n `5`; index avg `0.0013` n `23`; metal avg `0.0156` n `18`; unknown avg `-0.2862` n `376`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0369` n `228`; crypto_major avg `-0.1201` n `8`; equity avg `-0.0281` n `65`; fx avg `-0.0013` n `5`; index avg `-0.0096` n `23`; metal avg `-0.0043` n `18`; unknown avg `-0.5547` n `375`
- 4h: commodity avg `0.1846` n `12`; crypto_alt avg `0.2826` n `228`; crypto_major avg `0.3832` n `8`; equity avg `0.0062` n `65`; fx avg `0.0004` n `5`; index avg `0.1551` n `23`; metal avg `0.0733` n `18`; unknown avg `-0.571` n `375`
- 24h: commodity avg `-0.26` n `12`; crypto_alt avg `4.4783` n `228`; crypto_major avg `2.8199` n `8`; equity avg `3.4622` n `65`; fx avg `0.0488` n `5`; index avg `1.3694` n `23`; metal avg `0.1644` n `18`; unknown avg `1.3902` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
