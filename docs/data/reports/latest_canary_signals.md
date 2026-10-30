# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T05:52:27.965663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1863` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8934` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9827` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0403` n `13`; crypto_alt avg `-0.2661` n `238`; crypto_major avg `-0.2452` n `8`; equity avg `-0.2235` n `156`; fx avg `-0.0066` n `6`; index avg `-0.0253` n `27`; metal avg `-0.1068` n `20`; unknown avg `1.3921` n `1260`
- 1h: commodity avg `0.0321` n `13`; crypto_alt avg `0.3047` n `238`; crypto_major avg `0.2226` n `8`; equity avg `-0.5127` n `156`; fx avg `-0.013` n `6`; index avg `-0.0741` n `27`; metal avg `0.0057` n `20`; unknown avg `0.2259` n `1252`
- 4h: commodity avg `-0.2711` n `13`; crypto_alt avg `2.9927` n `238`; crypto_major avg `2.9152` n `8`; equity avg `0.9325` n `156`; fx avg `-0.0474` n `6`; index avg `0.0997` n `27`; metal avg `0.0218` n `20`; unknown avg `5.4426` n `1232`
- 24h: commodity avg `-0.0221` n `13`; crypto_alt avg `-3.8975` n `238`; crypto_major avg `-0.2953` n `8`; equity avg `-3.1174` n `155`; fx avg `0.1144` n `6`; index avg `-0.4222` n `27`; metal avg `-0.5794` n `20`; unknown avg `29.5147` n `980`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
