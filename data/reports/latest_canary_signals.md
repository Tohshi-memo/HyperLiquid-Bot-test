# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T16:37:37.042374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2318` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1164` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.094` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.4355` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0853` n `13`; crypto_alt avg `-0.3352` n `239`; crypto_major avg `-0.5272` n `8`; equity avg `-0.6545` n `166`; fx avg `0.0042` n `6`; index avg `-0.0716` n `27`; metal avg `-0.0219` n `20`; unknown avg `-0.3073` n `1266`
- 1h: commodity avg `-0.0132` n `13`; crypto_alt avg `-0.6643` n `239`; crypto_major avg `-1.563` n `8`; equity avg `-1.4441` n `166`; fx avg `-0.0473` n `6`; index avg `-0.1275` n `27`; metal avg `-0.0831` n `20`; unknown avg `0.469` n `1258`
- 4h: commodity avg `-0.6046` n `13`; crypto_alt avg `2.5123` n `239`; crypto_major avg `2.6272` n `8`; equity avg `4.7212` n `166`; fx avg `-0.2113` n `6`; index avg `0.5877` n `27`; metal avg `0.5108` n `20`; unknown avg `168.8126` n `1250`
- 24h: commodity avg `-1.5418` n `13`; crypto_alt avg `2.9689` n `239`; crypto_major avg `3.2013` n `8`; equity avg `6.2443` n `166`; fx avg `-0.0605` n `6`; index avg `0.568` n `27`; metal avg `0.7997` n `20`; unknown avg `244.8098` n `1061`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
