# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T14:07:46.325975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4253` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2762` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7215` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2` n `13`; crypto_alt avg `0.0336` n `238`; crypto_major avg `0.1192` n `8`; equity avg `0.477` n `156`; fx avg `0.0325` n `6`; index avg `0.0706` n `27`; metal avg `0.0068` n `20`; unknown avg `0.7091` n `1164`
- 1h: commodity avg `0.1533` n `13`; crypto_alt avg `0.0195` n `238`; crypto_major avg `0.1467` n `8`; equity avg `0.3621` n `156`; fx avg `0.0103` n `6`; index avg `-0.0391` n `27`; metal avg `-0.0958` n `20`; unknown avg `0.5753` n `1164`
- 4h: commodity avg `-0.2869` n `13`; crypto_alt avg `1.3202` n `238`; crypto_major avg `2.1384` n `8`; equity avg `0.4169` n `155`; fx avg `0.0101` n `6`; index avg `-0.0886` n `27`; metal avg `-0.1378` n `20`; unknown avg `6.7537` n `1086`
- 24h: commodity avg `-0.6196` n `13`; crypto_alt avg `-0.1499` n `238`; crypto_major avg `1.2372` n `8`; equity avg `-0.3111` n `155`; fx avg `-0.0267` n `6`; index avg `-0.1045` n `27`; metal avg `-0.5604` n `20`; unknown avg `8.3349` n `958`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
