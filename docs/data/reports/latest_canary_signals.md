# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T16:52:15.361933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5577` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5282` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `0.1794` n `228`; crypto_major avg `0.1654` n `8`; equity avg `0.0435` n `67`; fx avg `0.0` n `6`; index avg `0.0003` n `23`; metal avg `0.0126` n `18`; unknown avg `0.9464` n `396`
- 1h: commodity avg `-0.1852` n `12`; crypto_alt avg `0.4627` n `228`; crypto_major avg `0.2959` n `8`; equity avg `0.0822` n `67`; fx avg `-0.003` n `6`; index avg `-0.0774` n `23`; metal avg `0.0095` n `18`; unknown avg `1.0047` n `396`
- 4h: commodity avg `-0.802` n `12`; crypto_alt avg `2.4669` n `228`; crypto_major avg `1.7557` n `8`; equity avg `0.8235` n `67`; fx avg `0.0092` n `6`; index avg `0.2127` n `23`; metal avg `0.2275` n `18`; unknown avg `1.3446` n `396`
- 24h: commodity avg `0.0643` n `12`; crypto_alt avg `-2.8446` n `228`; crypto_major avg `-1.8681` n `8`; equity avg `-0.8369` n `67`; fx avg `0.0155` n `6`; index avg `-0.2261` n `23`; metal avg `-0.0886` n `18`; unknown avg `-0.5102` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
