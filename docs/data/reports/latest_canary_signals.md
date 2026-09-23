# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T15:07:35.375793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2898` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0347` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9821` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5611` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.4289` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0755` n `12`; crypto_alt avg `0.3518` n `234`; crypto_major avg `0.341` n `8`; equity avg `0.23` n `140`; fx avg `0.0106` n `6`; index avg `0.0317` n `26`; metal avg `0.034` n `20`; unknown avg `1.6208` n `942`
- 1h: commodity avg `0.0155` n `12`; crypto_alt avg `-1.8129` n `234`; crypto_major avg `-1.4445` n `8`; equity avg `0.0024` n `140`; fx avg `-0.0133` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0119` n `20`; unknown avg `4.7302` n `942`
- 4h: commodity avg `0.0834` n `12`; crypto_alt avg `-3.0683` n `234`; crypto_major avg `-2.2064` n `8`; equity avg `-0.6453` n `140`; fx avg `-0.0159` n `6`; index avg `-0.1717` n `26`; metal avg `-0.2243` n `20`; unknown avg `512.5078` n `898`
- 24h: commodity avg `0.2435` n `12`; crypto_alt avg `-0.2487` n `234`; crypto_major avg `-2.0731` n `8`; equity avg `-0.4461` n `140`; fx avg `0.0248` n `6`; index avg `-0.2059` n `26`; metal avg `-0.4796` n `20`; unknown avg `16.5045` n `830`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.251`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
