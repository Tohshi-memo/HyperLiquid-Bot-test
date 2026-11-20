# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T18:52:26.985802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.7786` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.0331` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.0195` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1776` n `13`; crypto_alt avg `-0.2545` n `239`; crypto_major avg `-0.4972` n `8`; equity avg `-0.026` n `166`; fx avg `-0.0023` n `6`; index avg `0.0006` n `27`; metal avg `-0.0189` n `20`; unknown avg `2.095` n `1262`
- 1h: commodity avg `0.1639` n `13`; crypto_alt avg `0.4491` n `239`; crypto_major avg `0.0264` n `8`; equity avg `0.2292` n `166`; fx avg `0.0111` n `6`; index avg `0.0305` n `27`; metal avg `-0.0063` n `20`; unknown avg `2.8353` n `1258`
- 4h: commodity avg `0.3597` n `13`; crypto_alt avg `-2.5248` n `239`; crypto_major avg `-3.4189` n `8`; equity avg `-3.3995` n `166`; fx avg `0.0163` n `6`; index avg `-0.3858` n `27`; metal avg `-0.3994` n `20`; unknown avg `3.0223` n `1247`
- 24h: commodity avg `-0.0247` n `13`; crypto_alt avg `-5.9084` n `239`; crypto_major avg `-7.1669` n `8`; equity avg `-7.8113` n `166`; fx avg `0.0004` n `6`; index avg `-0.7125` n `27`; metal avg `-1.3092` n `20`; unknown avg `49.0553` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
