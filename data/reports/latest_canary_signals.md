# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T12:37:25.132035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1564` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0178` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7389` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0166` n `13`; crypto_alt avg `0.0296` n `239`; crypto_major avg `0.0309` n `8`; equity avg `0.0229` n `162`; fx avg `0.009` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0088` n `20`; unknown avg `3.9377` n `1263`
- 1h: commodity avg `0.0212` n `13`; crypto_alt avg `0.2237` n `239`; crypto_major avg `-0.0836` n `8`; equity avg `-0.0414` n `162`; fx avg `0.0002` n `6`; index avg `-0.0086` n `27`; metal avg `0.0036` n `20`; unknown avg `0.1304` n `1253`
- 4h: commodity avg `-0.0299` n `13`; crypto_alt avg `1.9942` n `239`; crypto_major avg `2.1265` n `8`; equity avg `0.3876` n `162`; fx avg `-0.0127` n `6`; index avg `0.0394` n `27`; metal avg `0.1087` n `20`; unknown avg `0.4733` n `1253`
- 24h: commodity avg `0.0511` n `13`; crypto_alt avg `-3.5336` n `239`; crypto_major avg `-2.8296` n `8`; equity avg `-0.6736` n `162`; fx avg `0.0177` n `6`; index avg `-0.0612` n `27`; metal avg `-0.3203` n `20`; unknown avg `175.8732` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
