# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T20:52:45.139106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.0587` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.0469` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.8744` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6046` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0214` n `13`; crypto_alt avg `-0.2849` n `239`; crypto_major avg `-0.187` n `8`; equity avg `-0.4492` n `166`; fx avg `-0.0088` n `6`; index avg `-0.0524` n `27`; metal avg `-0.0633` n `20`; unknown avg `0.2346` n `1266`
- 1h: commodity avg `0.0538` n `13`; crypto_alt avg `-0.5417` n `239`; crypto_major avg `-0.4581` n `8`; equity avg `0.1536` n `166`; fx avg `0.0019` n `6`; index avg `0.0367` n `27`; metal avg `-0.015` n `20`; unknown avg `169.0697` n `1256`
- 4h: commodity avg `-0.0489` n `13`; crypto_alt avg `-2.1215` n `239`; crypto_major avg `-2.0958` n `8`; equity avg `-0.4912` n `166`; fx avg `-0.0144` n `6`; index avg `-0.0371` n `27`; metal avg `-0.2214` n `20`; unknown avg `165.0566` n `1258`
- 24h: commodity avg `-1.5225` n `13`; crypto_alt avg `0.8847` n `239`; crypto_major avg `1.2149` n `8`; equity avg `5.5764` n `166`; fx avg `-0.0847` n `6`; index avg `0.5373` n `27`; metal avg `0.5711` n `20`; unknown avg `70.3677` n `1062`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
