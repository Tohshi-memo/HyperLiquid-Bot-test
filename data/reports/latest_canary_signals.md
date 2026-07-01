# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T15:22:31.187018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3034` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.2355` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `-0.0222` n `228`; crypto_major avg `0.057` n `8`; equity avg `0.4325` n `88`; fx avg `-0.0092` n `6`; index avg `0.0557` n `25`; metal avg `-0.0328` n `20`; unknown avg `-0.0506` n `763`
- 1h: commodity avg `-0.1103` n `12`; crypto_alt avg `0.2658` n `228`; crypto_major avg `0.2234` n `8`; equity avg `-0.134` n `88`; fx avg `-0.0132` n `6`; index avg `-0.031` n `25`; metal avg `-0.2596` n `20`; unknown avg `-0.0566` n `763`
- 4h: commodity avg `-0.2286` n `12`; crypto_alt avg `1.5668` n `228`; crypto_major avg `2.0748` n `8`; equity avg `-0.1607` n `88`; fx avg `-0.0794` n `6`; index avg `-0.1618` n `25`; metal avg `0.6065` n `20`; unknown avg `0.3903` n `763`
- 24h: commodity avg `-0.7304` n `12`; crypto_alt avg `2.3895` n `228`; crypto_major avg `2.4041` n `8`; equity avg `0.4581` n `88`; fx avg `-0.0347` n `6`; index avg `-0.2672` n `25`; metal avg `0.3801` n `20`; unknown avg `0.5046` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
