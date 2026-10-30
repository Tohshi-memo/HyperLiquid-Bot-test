# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T06:22:28.240969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.3951` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3889` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.6571` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0049` n `13`; crypto_alt avg `0.1925` n `238`; crypto_major avg `0.2089` n `8`; equity avg `0.1593` n `156`; fx avg `-0.0111` n `6`; index avg `0.0334` n `27`; metal avg `0.0039` n `20`; unknown avg `0.1656` n `1260`
- 1h: commodity avg `0.0341` n `13`; crypto_alt avg `-0.1079` n `238`; crypto_major avg `0.063` n `8`; equity avg `-0.2125` n `156`; fx avg `-0.0039` n `6`; index avg `-0.016` n `27`; metal avg `-0.1184` n `20`; unknown avg `-0.1989` n `1238`
- 4h: commodity avg `-0.1626` n `13`; crypto_alt avg `2.2482` n `238`; crypto_major avg `2.2263` n `8`; equity avg `0.5692` n `156`; fx avg `-0.0538` n `6`; index avg `0.0839` n `27`; metal avg `-0.1688` n `20`; unknown avg `1.3585` n `1216`
- 24h: commodity avg `-0.0594` n `13`; crypto_alt avg `-3.3291` n `238`; crypto_major avg `0.373` n `8`; equity avg `-2.8658` n `155`; fx avg `0.1188` n `6`; index avg `-0.3682` n `27`; metal avg `-0.6324` n `20`; unknown avg `29.6656` n `980`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
