# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T19:22:34.187812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.21` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.1648` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0035` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9695` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6819` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0288` n `12`; crypto_alt avg `0.1733` n `233`; crypto_major avg `0.0756` n `8`; equity avg `-0.0184` n `136`; fx avg `0.0005` n `6`; index avg `0.0001` n `26`; metal avg `0.0357` n `20`; unknown avg `11.5501` n `806`
- 1h: commodity avg `0.051` n `12`; crypto_alt avg `-0.4132` n `233`; crypto_major avg `-0.2199` n `8`; equity avg `-0.185` n `136`; fx avg `0.0225` n `6`; index avg `-0.0225` n `26`; metal avg `0.0236` n `20`; unknown avg `0.1851` n `804`
- 4h: commodity avg `0.1161` n `12`; crypto_alt avg `-2.1203` n `233`; crypto_major avg `-2.0487` n `8`; equity avg `-0.3668` n `136`; fx avg `0.0229` n `6`; index avg `-0.0452` n `26`; metal avg `-0.0792` n `20`; unknown avg `1.8983` n `752`
- 24h: commodity avg `-0.4341` n `12`; crypto_alt avg `0.0265` n `233`; crypto_major avg `0.7874` n `8`; equity avg `0.4923` n `136`; fx avg `-0.1455` n `6`; index avg `0.3253` n `26`; metal avg `0.262` n `20`; unknown avg `5.0503` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
