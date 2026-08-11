# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T04:36:10.183586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `-0.1081` n `230`; crypto_major avg `-0.0354` n `8`; equity avg `0.0152` n `113`; fx avg `0.0045` n `6`; index avg `0.0152` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.167` n `785`
- 1h: commodity avg `-0.0432` n `12`; crypto_alt avg `-0.0861` n `230`; crypto_major avg `-0.0134` n `8`; equity avg `0.1806` n `113`; fx avg `-0.017` n `6`; index avg `0.0342` n `25`; metal avg `-0.0468` n `20`; unknown avg `1.2256` n `785`
- 4h: commodity avg `-0.028` n `12`; crypto_alt avg `-0.0315` n `230`; crypto_major avg `0.3664` n `8`; equity avg `0.5638` n `113`; fx avg `-0.0186` n `6`; index avg `0.1766` n `25`; metal avg `-0.0283` n `20`; unknown avg `-0.1365` n `785`
- 24h: commodity avg `0.8063` n `12`; crypto_alt avg `-0.6156` n `230`; crypto_major avg `-0.389` n `8`; equity avg `-0.7899` n `113`; fx avg `0.0966` n `6`; index avg `0.0965` n `25`; metal avg `0.4426` n `20`; unknown avg `103.9379` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
