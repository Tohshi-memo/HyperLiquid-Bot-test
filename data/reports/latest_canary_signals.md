# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T13:22:26.944209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5244` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0974` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.072` n `12`; crypto_alt avg `0.2083` n `229`; crypto_major avg `0.3113` n `8`; equity avg `0.2017` n `88`; fx avg `-0.0102` n `6`; index avg `0.028` n `25`; metal avg `-0.0275` n `20`; unknown avg `-0.0695` n `763`
- 1h: commodity avg `0.1264` n `12`; crypto_alt avg `0.4003` n `229`; crypto_major avg `0.6337` n `8`; equity avg `0.4786` n `88`; fx avg `0.0507` n `6`; index avg `0.0741` n `25`; metal avg `0.5292` n `20`; unknown avg `-0.2247` n `763`
- 4h: commodity avg `0.0276` n `12`; crypto_alt avg `1.5555` n `228`; crypto_major avg `2.552` n `8`; equity avg `1.2819` n `88`; fx avg `0.0132` n `6`; index avg `0.2081` n `25`; metal avg `0.4546` n `20`; unknown avg `-0.2604` n `763`
- 24h: commodity avg `-0.433` n `12`; crypto_alt avg `3.4395` n `228`; crypto_major avg `4.5802` n `8`; equity avg `0.2312` n `88`; fx avg `-0.0207` n `6`; index avg `-0.2873` n `25`; metal avg `1.0286` n `20`; unknown avg `1.7986` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
