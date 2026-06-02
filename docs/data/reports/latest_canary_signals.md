# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T06:37:19.715111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.72` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.284` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8423` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4422` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `0.3431` n `228`; crypto_major avg `0.1654` n `8`; equity avg `0.0402` n `69`; fx avg `0.0229` n `6`; index avg `0.012` n `23`; metal avg `0.0078` n `18`; unknown avg `-0.0154` n `422`
- 1h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.1768` n `228`; crypto_major avg `-0.2521` n `8`; equity avg `0.0336` n `69`; fx avg `0.0664` n `6`; index avg `0.0755` n `23`; metal avg `0.0865` n `18`; unknown avg `-0.4673` n `412`
- 4h: commodity avg `-0.3753` n `12`; crypto_alt avg `-0.2272` n `228`; crypto_major avg `-1.0386` n `8`; equity avg `0.8037` n `69`; fx avg `0.0776` n `6`; index avg `0.4036` n `23`; metal avg `1.2454` n `18`; unknown avg `-0.103` n `412`
- 24h: commodity avg `-1.0601` n `12`; crypto_alt avg `-0.0252` n `228`; crypto_major avg `-1.436` n `8`; equity avg `0.1686` n `69`; fx avg `0.177` n `6`; index avg `-0.2677` n `23`; metal avg `1.1047` n `18`; unknown avg `1.901` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
