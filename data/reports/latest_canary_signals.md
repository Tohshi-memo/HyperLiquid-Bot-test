# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T07:37:28.129828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5349` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5295` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0592` n `12`; crypto_alt avg `-0.0972` n `228`; crypto_major avg `-0.203` n `8`; equity avg `-0.2253` n `86`; fx avg `-0.019` n `6`; index avg `-0.0145` n `23`; metal avg `-0.0967` n `20`; unknown avg `-0.0575` n `620`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `0.2922` n `228`; crypto_major avg `0.0856` n `8`; equity avg `0.3131` n `86`; fx avg `-0.0623` n `6`; index avg `0.1136` n `23`; metal avg `0.0428` n `20`; unknown avg `-0.0859` n `620`
- 4h: commodity avg `-0.129` n `12`; crypto_alt avg `-1.6598` n `228`; crypto_major avg `-1.8144` n `8`; equity avg `-0.8992` n `86`; fx avg `-0.015` n `6`; index avg `-0.2795` n `23`; metal avg `-0.2849` n `20`; unknown avg `0.1992` n `604`
- 24h: commodity avg `-0.7589` n `12`; crypto_alt avg `-2.881` n `228`; crypto_major avg `-2.8498` n `8`; equity avg `-4.0094` n `85`; fx avg `-0.0618` n `6`; index avg `-0.7631` n `23`; metal avg `-1.3834` n `18`; unknown avg `0.8282` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
