# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T23:37:32.054024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1092` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1059` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `0.1414` n `239`; crypto_major avg `0.169` n `8`; equity avg `0.0729` n `163`; fx avg `0.0006` n `6`; index avg `0.0093` n `27`; metal avg `-0.004` n `20`; unknown avg `1.7784` n `1265`
- 1h: commodity avg `0.066` n `13`; crypto_alt avg `0.6723` n `239`; crypto_major avg `0.8598` n `8`; equity avg `0.9402` n `163`; fx avg `-0.0031` n `6`; index avg `0.0784` n `27`; metal avg `0.0421` n `20`; unknown avg `1.3636` n `1223`
- 4h: commodity avg `0.0689` n `13`; crypto_alt avg `2.1032` n `239`; crypto_major avg `2.1781` n `8`; equity avg `3.3006` n `163`; fx avg `-0.0194` n `6`; index avg `0.3194` n `27`; metal avg `0.0722` n `20`; unknown avg `3.2609` n `1193`
- 24h: commodity avg `0.3149` n `13`; crypto_alt avg `1.8062` n `239`; crypto_major avg `1.6803` n `8`; equity avg `2.2169` n `163`; fx avg `0.0203` n `6`; index avg `0.1781` n `27`; metal avg `0.057` n `20`; unknown avg `8.145` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
