# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T20:22:26.165305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.1451` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8754` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0066` n `228`; crypto_major avg `-0.1428` n `8`; equity avg `0.0448` n `88`; fx avg `0.0049` n `6`; index avg `0.0068` n `23`; metal avg `0.0469` n `20`; unknown avg `-0.1382` n `765`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `-0.1023` n `228`; crypto_major avg `-0.005` n `8`; equity avg `0.1061` n `88`; fx avg `0.0103` n `6`; index avg `0.024` n `23`; metal avg `0.0497` n `20`; unknown avg `0.0923` n `765`
- 4h: commodity avg `-0.0942` n `12`; crypto_alt avg `0.8841` n `228`; crypto_major avg `2.0509` n `8`; equity avg `1.0612` n `88`; fx avg `-0.0148` n `6`; index avg `0.1189` n `23`; metal avg `0.1755` n `20`; unknown avg `1.3433` n `765`
- 24h: commodity avg `-0.5715` n `12`; crypto_alt avg `1.6654` n `228`; crypto_major avg `2.8943` n `8`; equity avg `1.7077` n `88`; fx avg `0.1503` n `6`; index avg `0.2161` n `23`; metal avg `-0.4636` n `20`; unknown avg `2.3182` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
