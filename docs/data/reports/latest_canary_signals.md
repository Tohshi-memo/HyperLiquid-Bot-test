# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T07:52:26.939153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0806` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7703` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5913` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `-0.1983` n `228`; crypto_major avg `-0.1694` n `8`; equity avg `-0.2138` n `86`; fx avg `0.0053` n `6`; index avg `-0.0254` n `23`; metal avg `-0.1846` n `20`; unknown avg `-0.0506` n `764`
- 1h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.0222` n `228`; crypto_major avg `-0.1987` n `8`; equity avg `-0.1138` n `86`; fx avg `-0.0485` n `6`; index avg `0.0031` n `23`; metal avg `-0.1872` n `20`; unknown avg `-0.0973` n `620`
- 4h: commodity avg `-0.056` n `12`; crypto_alt avg `-2.0523` n `228`; crypto_major avg `-2.1366` n `8`; equity avg `-1.4198` n `86`; fx avg `0.0066` n `6`; index avg `-0.3663` n `23`; metal avg `-0.5453` n `20`; unknown avg `0.1982` n `604`
- 24h: commodity avg `-0.7882` n `12`; crypto_alt avg `-2.9602` n `228`; crypto_major avg `-2.905` n `8`; equity avg `-4.1928` n `85`; fx avg `-0.0445` n `6`; index avg `-0.7782` n `23`; metal avg `-1.5254` n `18`; unknown avg `0.7756` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
