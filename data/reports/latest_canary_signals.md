# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T05:22:25.887438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.8257` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.7111` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.6058` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0274` n `13`; crypto_alt avg `0.2754` n `238`; crypto_major avg `0.1371` n `8`; equity avg `-0.1663` n `156`; fx avg `-0.0077` n `6`; index avg `-0.0217` n `27`; metal avg `-0.0236` n `20`; unknown avg `226.7209` n `1260`
- 1h: commodity avg `-0.0488` n `13`; crypto_alt avg `0.8713` n `238`; crypto_major avg `0.5084` n `8`; equity avg `-0.044` n `156`; fx avg `-0.0094` n `6`; index avg `-0.0204` n `27`; metal avg `0.0368` n `20`; unknown avg `0.294` n `1254`
- 4h: commodity avg `0.0735` n `13`; crypto_alt avg `2.7229` n `238`; crypto_major avg `2.7846` n `8`; equity avg `1.1788` n `156`; fx avg `-0.0703` n `6`; index avg `0.1021` n `27`; metal avg `-0.0411` n `20`; unknown avg `4.768` n `1234`
- 24h: commodity avg `-0.088` n `13`; crypto_alt avg `-3.9728` n `238`; crypto_major avg `-0.2752` n `8`; equity avg `-3.0918` n `155`; fx avg `0.1115` n `6`; index avg `-0.4195` n `27`; metal avg `-0.7093` n `20`; unknown avg `29.4616` n `982`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
