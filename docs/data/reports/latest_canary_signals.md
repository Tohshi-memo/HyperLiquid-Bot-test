# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T07:07:17.331264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.527` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.398` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0835` n `12`; crypto_alt avg `-0.018` n `228`; crypto_major avg `0.029` n `8`; equity avg `0.2232` n `67`; fx avg `0.0169` n `6`; index avg `0.0644` n `23`; metal avg `0.1047` n `18`; unknown avg `-0.0779` n `419`
- 1h: commodity avg `-0.0518` n `12`; crypto_alt avg `0.1224` n `228`; crypto_major avg `0.188` n `8`; equity avg `0.2441` n `67`; fx avg `0.0305` n `6`; index avg `0.1457` n `23`; metal avg `0.3249` n `18`; unknown avg `0.8999` n `419`
- 4h: commodity avg `-0.0108` n `12`; crypto_alt avg `-2.6328` n `228`; crypto_major avg `-1.4738` n `8`; equity avg `-0.1189` n `67`; fx avg `-0.0447` n `6`; index avg `-0.0758` n `23`; metal avg `0.0532` n `18`; unknown avg `0.3397` n `409`
- 24h: commodity avg `0.2695` n `12`; crypto_alt avg `-5.1245` n `228`; crypto_major avg `-3.7866` n `8`; equity avg `-1.1175` n `67`; fx avg `-0.1273` n `6`; index avg `-0.7734` n `23`; metal avg `-1.4007` n `18`; unknown avg `-0.9991` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
