# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T05:15:36.753739+00:00`
- Correlation status: `ready`
- Asset price records: `236`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5174` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3436` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8226` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.113` n `7`; crypto_alt avg `-0.2651` n `223`; crypto_major avg `-0.2343` n `7`; equity avg `0.04` n `42`; fx avg `-0.0032` n `4`; index avg `-0.01` n `9`; metal avg `-0.0568` n `7`; unknown avg `0.2029` n `314`
- 1h: commodity avg `-0.0275` n `7`; crypto_alt avg `-0.2218` n `223`; crypto_major avg `-0.0946` n `7`; equity avg `-0.104` n `42`; fx avg `0.0226` n `4`; index avg `-0.0107` n `9`; metal avg `-0.2054` n `7`; unknown avg `0.0219` n `314`
- 4h: commodity avg `0.004` n `7`; crypto_alt avg `1.9635` n `223`; crypto_major avg `2.5214` n `7`; equity avg `0.6988` n `42`; fx avg `-0.0371` n `4`; index avg `0.5748` n `9`; metal avg `0.1778` n `7`; unknown avg `0.2067` n `314`
- 24h: commodity avg `-0.0106` n `7`; crypto_alt avg `2.5206` n `223`; crypto_major avg `2.9496` n `7`; equity avg `1.2092` n `42`; fx avg `-0.0482` n `4`; index avg `0.8737` n `9`; metal avg `0.1618` n `7`; unknown avg `0.4233` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3907`, n `228`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3807`, n `228`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3654`, n `232`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3502`, n `232`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2003`, n `232`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1891`, n `228`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1885`, n `228`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `232`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.174`, n `232`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1582`, n `228`, weak_sample_signal
