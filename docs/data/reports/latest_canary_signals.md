# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T04:22:26.264802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.2468` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.0287` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9388` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.0431` n `239`; crypto_major avg `-0.0586` n `8`; equity avg `0.0493` n `162`; fx avg `-0.0046` n `6`; index avg `0.0088` n `27`; metal avg `-0.0573` n `20`; unknown avg `8.3246` n `1256`
- 1h: commodity avg `0.0332` n `13`; crypto_alt avg `-0.2725` n `239`; crypto_major avg `-0.422` n `8`; equity avg `-0.4453` n `162`; fx avg `0.0014` n `6`; index avg `-0.0592` n `27`; metal avg `-0.0784` n `20`; unknown avg `-0.1412` n `1248`
- 4h: commodity avg `-0.0661` n `13`; crypto_alt avg `-2.4853` n `239`; crypto_major avg `-3.0948` n `8`; equity avg `-1.7198` n `162`; fx avg `-0.0181` n `6`; index avg `-0.156` n `27`; metal avg `0.152` n `20`; unknown avg `0.551` n `1245`
- 24h: commodity avg `0.9238` n `13`; crypto_alt avg `-2.9154` n `239`; crypto_major avg `-4.3505` n `8`; equity avg `-1.5909` n `162`; fx avg `0.0059` n `6`; index avg `-0.058` n `27`; metal avg `-0.4325` n `20`; unknown avg `99.5427` n `1121`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
