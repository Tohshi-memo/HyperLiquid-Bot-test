# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T18:07:34.330907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.23` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.3178` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.246` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0327` n `12`; crypto_alt avg `-0.0058` n `228`; crypto_major avg `-0.1411` n `8`; equity avg `-0.0049` n `88`; fx avg `-0.0014` n `6`; index avg `0.0036` n `23`; metal avg `0.0644` n `20`; unknown avg `0.239` n `765`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `0.642` n `228`; crypto_major avg `0.9603` n `8`; equity avg `0.2364` n `88`; fx avg `-0.0108` n `6`; index avg `0.0157` n `23`; metal avg `0.2294` n `20`; unknown avg `0.2457` n `765`
- 4h: commodity avg `0.1274` n `12`; crypto_alt avg `1.7295` n `228`; crypto_major avg `2.4452` n `8`; equity avg `2.3263` n `88`; fx avg `-0.0097` n `6`; index avg `0.2812` n `23`; metal avg `0.1992` n `20`; unknown avg `2.8467` n `764`
- 24h: commodity avg `-0.5007` n `12`; crypto_alt avg `1.7901` n `228`; crypto_major avg `2.5662` n `8`; equity avg `1.3882` n `88`; fx avg `0.1302` n `6`; index avg `0.1502` n `23`; metal avg `-0.418` n `20`; unknown avg `3.6349` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
