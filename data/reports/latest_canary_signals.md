# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T14:52:48.611636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `12`; crypto_alt avg `-0.1835` n `230`; crypto_major avg `-0.1852` n `8`; equity avg `-0.2952` n `113`; fx avg `-0.0015` n `6`; index avg `-0.0249` n `25`; metal avg `0.001` n `20`; unknown avg `0.0199` n `784`
- 1h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.0759` n `230`; crypto_major avg `0.2126` n `8`; equity avg `0.1437` n `113`; fx avg `0.0069` n `6`; index avg `0.0503` n `25`; metal avg `0.2251` n `20`; unknown avg `0.1513` n `784`
- 4h: commodity avg `0.3913` n `12`; crypto_alt avg `-0.2934` n `230`; crypto_major avg `-0.4358` n `8`; equity avg `-0.7641` n `113`; fx avg `0.0435` n `6`; index avg `-0.0358` n `25`; metal avg `0.0889` n `20`; unknown avg `0.2556` n `784`
- 24h: commodity avg `1.0309` n `12`; crypto_alt avg `0.1448` n `230`; crypto_major avg `-0.7274` n `8`; equity avg `-1.0329` n `113`; fx avg `0.2622` n `6`; index avg `0.0091` n `25`; metal avg `-0.0798` n `20`; unknown avg `103.6412` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
