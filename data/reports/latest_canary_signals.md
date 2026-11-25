# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T17:52:29.922255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.4503` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3769` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `0.2437` n `239`; crypto_major avg `0.2656` n `8`; equity avg `0.5936` n `168`; fx avg `0.0026` n `6`; index avg `0.0602` n `27`; metal avg `0.0849` n `20`; unknown avg `158.1625` n `1267`
- 1h: commodity avg `0.2353` n `13`; crypto_alt avg `2.1624` n `239`; crypto_major avg `2.0561` n `8`; equity avg `3.3045` n `168`; fx avg `0.0345` n `6`; index avg `0.3738` n `27`; metal avg `0.6215` n `20`; unknown avg `24.1754` n `1262`
- 4h: commodity avg `0.3064` n `13`; crypto_alt avg `2.5584` n `239`; crypto_major avg `2.6833` n `8`; equity avg `1.6959` n `168`; fx avg `0.077` n `6`; index avg `0.2203` n `27`; metal avg `0.233` n `20`; unknown avg `404.2087` n `1243`
- 24h: commodity avg `0.4721` n `13`; crypto_alt avg `0.36` n `239`; crypto_major avg `-0.4533` n `8`; equity avg `-2.7208` n `168`; fx avg `-0.0097` n `6`; index avg `-0.2705` n `27`; metal avg `-0.4559` n `20`; unknown avg `633.3639` n `1077`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
